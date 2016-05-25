from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response  import Response
from rest_framework.parsers import JSONParser, BaseParser
from api.serializers import UserSerializer
from rest_framework import permissions
from django.conf import settings
import hashlib
import uuid
from os import path

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

  def post(self, request):
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

