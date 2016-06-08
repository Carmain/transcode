"""
Django settings for api project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import datetime
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm=#v%3@joh!4j6rhivbclt2#n4v2a%9cbfv1x&z!&^4!u4^nse'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'api',
    'rest_framework'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'transcode.urls'

WSGI_APPLICATION = 'transcode.wsgi.application'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
AUTH_USER_MODEL = "api.User"
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

JWT_AUTH = {
  'JWT_ALLOW_REFRESH': True,
  'JWT_AUTH_HEADER_PREFIX': 'JWT',
  'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1)
}

# (extension, name)
SUPPORTED_FILES = (
    ("mvk", "Matroska"),
    ("mp3", "MPEG 3"),
    ("mp4", "MPEG 4"),
    ("avi", "Audio Video Interleaved"),
    ("wav", "Wave"),
    ("ogg", "Theora Vorbis"),
)

# (format, codec)
VIDEO_TYPES = (
  ("mkv", "h264"),
  ("avi", "divx"),
  ("mp4", "h264"),
)

AUDIO_TYPES = (
  ("mp3", "mp3"),
  ("ogg", "vorbis"),
  ("mp4", "aac"),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

try:
    from transcode.local_settings import *
except ImportError:
    raise ImportError("Check that you have correctly renamed local_settings.py.template file.")
