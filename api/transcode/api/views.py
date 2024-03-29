import mimetypes
import hashlib
import uuid
import datetime
import re
import json
import braintree

from worker.main import convert
from api.models import User, TranscodeFile, UploadSession, ConvertedFile
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, BaseParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from api.serializers import UserSerializer, ConvertedFileSerializer
from rest_framework import permissions
from urllib.request import urlopen
from urllib.parse import urlencode
from api.utils import get_price
from django.db.models import F
from django.conf import settings
from os import path
from django.http import StreamingHttpResponse, HttpResponse
from wsgiref.util import FileWrapper


@permission_classes((AllowAny, ))
class Register(APIView):
    def post(self, request):

        raw_date = request.data.get('birthdate')
        email = request.data.get('email')
        username = request.data.get('username')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')
        password_confirmation = request.data.get('password_confirmation')
        recaptcha_verify = request.data.get('recaptcha_verify')

        errors = []
        failure = False

        if not first_name:
            failure = True
            errors.append('Missing first name')

        if not last_name:
            failure = True
            errors.append('Missing last name')

        if not username:
            failure = True
            errors.append('Missing username')
        else:
            if User.objects.filter(username=username).exists():
                failure = True
                errors.append('This username is already used')
            else:
                reg_username = re.compile("[a-zA-Z0-9_-]{3,16}")
                if not reg_username.match(username):
                    failure = True
                    errors.append('The username is not valid')

        if not email:
            failure = True
            errors.append('Missing email')
        elif User.objects.filter(email=email).exists():
            failure = True
            errors.append('Wrong email')

        if not password:
            failure = True
            errors.append("Missing password")
        elif not password_confirmation:
            failure = True
            errors.append("Missing password confirmation")
        elif password != password_confirmation:
            failure = True
            errors.append("Password and password confirmation aren't equals")

        # ReCaptcha
        ip_address = request.META.get('REMOTE_ADDR')
        values = {
            "secret": settings.RECAPTCHA_PRIVATE_KEY,
            "response": recaptcha_verify,
            "remoteip": ip_address
        }

        data = urlencode(values)
        binary_data = data.encode('ascii')
        result = urlopen('https://www.google.com/recaptcha/api/siteverify',
                         binary_data)
        result_tostring = result.read().decode('utf-8')
        json_result = json.loads(result_tostring)

        if not recaptcha_verify:
            failure = True
            errors.append('You need to valid the ReCaptcha')
        elif not json_result['success']:
            failure = True
            errors.append('Are you a robot ?')

        if (failure):
            return Response({
                'success': False,
                'error_messages': errors
            }, status=status.HTTP_400_BAD_REQUEST)

        user, created = User.objects.get_or_create(
            email=request.data.get('email'),
            username=request.data.get('username'),
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name'),
            birthdate=datetime.datetime.strptime(raw_date, "%Y-%m-%d").date()
        )

        if created:
            user.set_password(request.data.get('password'))
            user.save()
            return Response(
                {'success': True},
                status=status.HTTP_201_CREATED
            )


class BinaryParser(BaseParser):
    media_type = 'application/octet-stream'

    def parse(self, stream, media_type=None, parser_context=None):
        return stream.read()


class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


@permission_classes((AllowAny, ))
class UploadStart(APIView):
    parser_classes = (JSONParser,)

    def post(self, request):
        file_size = request.data.get("fileSize")
        file_name = path.splitext(request.data.get("fileName"))[0]
        transcodeFile = TranscodeFile.objects.create(size=file_size, name=file_name)
        uploadSession = UploadSession.objects.create(file=transcodeFile)

        return Response({
            'success': True,
            'uuid': uploadSession.uuid,
            'chunkSize': settings.UPLOAD_CHUNK_SIZE
        })


@permission_classes((AllowAny, ))
class UploadChunk(APIView):
    parser_classes = (BinaryParser,)

    # TODO : Compare received chunk size with settings.UPLOAD_CHUNK_SIZE
    def post(self, request, uuid):
        uploadSessions = UploadSession.objects.filter(uuid=uuid)
        uploadSession = uploadSessions[0]
        userFile = open(uploadSession.file.path, "ab")
        userFile.write(request.data)
        uploadSessions.update(
          state=1,
          receivedBytes = F("receivedBytes") + len(request.data)
        )
        uploadSession.refresh_from_db()

        return Response({'success': True,
                         'remains': uploadSession.remainingBytes})


@permission_classes((AllowAny, ))
class UploadEnd(APIView):
    parser_classes = (JSONParser, )

    def post(self, request, uuid):
        uploadSession = UploadSession.objects.get(uuid=uuid)
        user_file_md5 = request.data.get("md5")
        hash_md5 = hashlib.md5()
        fpath = uploadSession.file.path
        with open(fpath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)

        hash_md5 = hash_md5.hexdigest()

        if user_file_md5 != hash_md5:
          return Response({'success': False, 'message': 'Bad MD5 hash'})

        uploaded_file = uploadSession.file

        uploadSession.state = 3
        uploadSession.save()
        try:
          uploaded_file.fetchMetaDatas()
        except TypeError as e:
          return Response({'success': False, 'message': str(e)})

        if uploaded_file.media_type == "video":
          available_types = settings.VIDEO_TYPES
        elif uploaded_file.media_type == "audio":
          available_types = settings.AUDIO_TYPES

        return Response({
          'success': True,
          'file_uuid': uploaded_file.uuid,
          'price': get_price(uploaded_file.duration / 60),
          "available_types": available_types
        })


@permission_classes((IsAuthenticated, ))
class getPaypalToken(APIView):
    parser_classes = (JSONParser, )

    def get(self, request):
        gateway = braintree.BraintreeGateway(
            access_token=settings.PAYPAL_ACCESS_TOKEN)
        token = gateway.client_token.generate()

        return Response({'success': True, 'token': token})


@permission_classes((IsAuthenticated, ))
class launch_conversion(APIView):
    parser_classes = (JSONParser, )

    def post(self, request):
        file_to_convert = TranscodeFile.objects.get(uuid=request.data.get("file"))
        dest_format = request.data.get("format")
        dest_codec = request.data.get("codec")
        dest_type = (dest_format, dest_codec)
        audio_only = (dest_format == "Audio")

        if audio_only:
            dest_type = ("mp3", "mp3")

        convert.delay(
            filePath=file_to_convert.path,
            fileUUID=file_to_convert.uuid,
            dest_type=dest_type,
            audio_only=audio_only
        )
        return Response({'success': True})


@permission_classes((IsAuthenticated, ))
class checkout(APIView):
    parser_classes = (JSONParser, )

    def post(self, request):
        transcode_file = TranscodeFile.objects.get(uuid=request.data.get('fileUUID'))
        price = get_price(transcode_file.duration / 60)
        gateway = braintree.BraintreeGateway(
            access_token=settings.PAYPAL_ACCESS_TOKEN)
        payment_method_nonce = request.data.get("payment_method_nonce")
        result = gateway.transaction.sale({
            "amount": str(price),
            "payment_method_nonce": payment_method_nonce,
            "order_id": uuid.uuid4().hex,
            "descriptor": {
              "name": "transco*conversion"
            },
            "options": {
              "paypal": {
                "custom_field": "PayPal custom field",
                "description": "Description for PayPal email receipt"
              },
            }
        })
        if result.is_success:
            transcode_file.owner = request.user
            transcode_file.save()
            return Response({'success': True,
                             'transaction': result.transaction.id})
        else:
            return Response({'success': False, 'message': result.message})


@permission_classes((AllowAny, ))
class statistics(APIView):
    parser_context = (JSONParser, )

    def get(self, request):
        converted_files = ConvertedFile.objects.all().count()
        users = User.objects.all().count()

        return Response({"converted_files": converted_files, "users": users})


class get_converted_files(APIView):
  parser_context = (JSONParser, )

  def get(self, request, limit=15):
      limit = int(limit)
      files = ConvertedFile.objects.filter(transcode_file__in=request.user.transcodefile_set.all())[:limit]
      serializer = ConvertedFileSerializer(files, many=True)
      return Response(serializer.data)

class delete_converted_file(APIView):
  parser_context = (JSONParser, )

  def delete(self, request, uuid):
    file_to_delete = request.user.transcodefile_set.filter(uuid=uuid)
    deleted_obj = file_to_delete.delete()

    if deleted_obj == 0:
      return Response({'success': False})

    return Response({'success': True})


@permission_classes((AllowAny, ))
class download_converted_file(APIView):
  def get(self, request, uuid):
    conv_file = ConvertedFile.objects.get(file_uuid=uuid)
    file_path = conv_file.path
    filename = "{}.{}".format(conv_file.transcode_file.name, conv_file.fileType)
    chunk_size = 8192
    fw = FileWrapper(open(file_path, 'rb'), chunk_size)
    response = StreamingHttpResponse(
      fw,
      content_type=mimetypes.guess_type(file_path)[0]
    )
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

class update_profile(APIView):
  def post(self, request):
    usr = request.user
    for key,value in request.data.items():
      if key == "birthdate":
        usr.birthdate = datetime.datetime.strptime(value, "%Y-%m-%d").date()
        continue

      if value != "":
        setattr(usr, key, value)

    usr.save()
    return Response({'success': True})

class update_password(APIView):
  def post(self, request):
    old_password = request.data.get("oldPassword")
    new_password = request.data.get("newPassword")
    if not request.user.check_password(old_password):
      return Response({'success': False, 'message': 'Wrong Password.'})

    request.user.set_password(new_password)
    request.user.save()

    return Response({'success': True})
