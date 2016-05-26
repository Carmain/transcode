from api.models import User
from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'email', 'username', 'last_login',
              'first_name', 'last_name', 'birthdate')
    read_only_fields = ('last_login', 'id',)
