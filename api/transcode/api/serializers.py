from api.models import User, TranscodeFile, ConvertedFile
from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'email', 'username', 'last_login',
              'first_name', 'last_name', 'birthdate',
              'disk_space', 'free_space', 'used_space')
    read_only_fields = ('last_login', 'id',)


class TranscodeFileSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = TranscodeFile
    fields = ('fileType', 'name', 'duration', 'size', 'media_type', 'uuid')


class ConvertedFileSerializer(serializers.HyperlinkedModelSerializer):
  transcode_file = TranscodeFileSerializer(read_only=True)
  class Meta:
    model = ConvertedFile
    fields = ('fileType', 'date', 'transcode_file', 'file_uuid')
