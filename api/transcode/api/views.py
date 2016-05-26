import hashlib
import uuid
import datetime
import re

from api.models import User
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, BaseParser
from rest_framework.permissions import AllowAny
from api.serializers import UserSerializer
from rest_framework import permissions
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

        if not first_name:
            return Response({
                'success': False,
                'error_msg': 'Missing first name'
            })

        if not last_name:
            return Response({
                'success': False,
                'error_msg': 'Missing last name'
            })

        if not username:
            return Response({
                'success': False,
                'error_msg': 'Missing username'
            })
        else:
            if User.objects.filter(username=username).exists():
                return Response({
                    'success': False,
                    'error_msg': 'This username is already used'
                })
            else:
                reg_username = re.compile("[a-zA-Z0-9_-]{3,16}")
                if not reg_username.match(username):
                    return Response({
                        'success': False,
                        'error_msg': 'The username is not a valid'
                    })

        if not email:
            return Response({
                'success': False,
                'error_msg': 'Missing email'
            })
        else:
            if User.objects.filter(email=email).exists():
                return Response({
                    'success': False,
                    'error_msg': 'This email is already used'
                })

        if not password:
            return Response({
                'success': False,
                'error_msg': 'Missing password'
            })
        elif not password_confirmation:
            return Response({
                'success': False,
                'error_msg': 'Missing password confirmation'
            })
        elif password != password_confirmation:
            return Response({
                'success': False,
                'error_msg': "Password and password confirmation aren't equals"
            })

        user = User.objects.create(
            email=request.data.get('email'),
            username=request.data.get('username'),
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name'),
            birthdate=datetime.datetime.strptime(raw_date, "%Y-%m-%d").date()
        )

        user.set_password(request.data.get('password'))
        user.save()

        return Response({'success': True})


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
    fileUUID = uuid.uuid4().hex
    filePath = path.join(settings.UPLOAD_DIRECTORY, fileUUID)

    return Response({
      'uuid': fileUUID
    })


class UploadChunk(APIView):
  parser_classes = (BinaryParser,)

  def post(self, request, uuid):
    fpath = path.join(settings.UPLOAD_DIRECTORY, uuid)
    userFile = open(fpath, "ab")
    userFile.write(bytes(request.data))

    return Response({'success': True})


class UploadEnd(APIView):
  parser_classes = (JSONParser, )

  def post(self, request, uuid):
    user_file_md5 = request.data.get("md5")
    hash_md5 = hashlib.md5()
    fpath = path.join(settings.UPLOAD_DIRECTORY, uuid)
    with open(fpath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)

    hash_md5 = hash_md5.hexdigest()
    success = user_file_md5 == hash_md5

    return Response({'success': success})
