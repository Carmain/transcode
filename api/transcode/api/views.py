from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response  import Response
from api.serializers import UserSerializer
from rest_framework import permissions

class CurrentUserView(APIView):
  def get(self, request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
