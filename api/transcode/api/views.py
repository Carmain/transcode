import hashlib
import uuid
import datetime
import re
import json

from api.models import User, TranscodeFile, UploadSession
from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, BaseParser
from rest_framework.permissions import AllowAny
from api.serializers import UserSerializer
from rest_framework import permissions
from urllib.request import urlopen
from urllib.parse import urlencode
from django.conf import settings
from os import path


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
            errors.append('Missing email')

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
        result = urlopen('https://www.google.com/recaptcha/api/siteverify', binary_data)
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


class UploadStart(APIView):
    parser_classes = (JSONParser,)

    def get(self, request):
        transcodeFile = TranscodeFile.objects.create()
        uploadSession = UploadSession.objects.create(file=transcodeFile)

        return Response({
            'success': True,
            'uuid': uploadSession.uuid,
            'chunkSize': settings.UPLOAD_CHUNK_SIZE
        })


class UploadChunk(APIView):
    parser_classes = (BinaryParser,)

    #TODO : Compare received chunk size with settings.UPLOAD_CHUNK_SIZE
    def post(self, request, uuid):
        uploadSession = UploadSession.objects.get(uuid=uuid)
        userFile = open(uploadSession.file.path, "ab")
        userFile.write(request.data)

        uploadSession.state = 1
        uploadSession.receivedBytes = len(request.data)
        uploadSession.save()

        return Response({'success': True, 'remains': uploadSession.remainingBytes})


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
        success = user_file_md5 == hash_md5

        if success:
            uploadSession.state = 3
            uploadSession.save()
            uploadSession.file.reloadFileType()

        return Response({'success': success})
