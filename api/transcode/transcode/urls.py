from api import urls
from django.conf.urls import url, include


urlpatterns = [
    url(r'api/', include(urls.urlpatterns)),
]
