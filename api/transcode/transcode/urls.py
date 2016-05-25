from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework import routers
from django.conf.urls import url, include
from api import views as api_views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^api-auth/', include("rest_framework.urls", namespace="rest_framework")),
    url(r'^auth/$', obtain_jwt_token),
    url(r'^refresh-jwt/$', refresh_jwt_token),
    url(r'^me/$', api_views.CurrentUserView.as_view()),
]
