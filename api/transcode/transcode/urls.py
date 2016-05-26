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
    url(r'^register/', api_views.Register.as_view()),
    url(r'^upload-start/$', api_views.UploadStart.as_view()),
    url(r'^upload-chunk/(?P<uuid>[0-9a-f]{32})/$', api_views.UploadChunk.as_view()),
    url(r'^upload-end/(?P<uuid>[0-9a-f]{32})/$', api_views.UploadEnd.as_view()),
]
