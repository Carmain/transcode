import uuid
import magic
from os import path
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

def generate_uuid4():
    return uuid.uuid4().hex

class User(AbstractUser):
    # first_name, last_name and username, password, email are already defined
    # in AbstractUser
    birthdate = models.DateTimeField(default=None, blank=True, null=True)


class TranscodeFile(models.Model):
    owner = models.ForeignKey("User", default=None, null=True, blank=True)
    uuid = models.CharField(default=generate_uuid4, max_length=32)
    fileType = models.CharField(choices=settings.SUPPORTED_FILES, default="tmp", max_length=3)
    size = models.IntegerField(default=9999999) # TODO Get realSize from client

    @property
    def path(self):
      return path.join(settings.UPLOAD_DIRECTORY, self.fileName)

    @property
    def fileName(self):
      return "{0}.{1}".format(self.uuid, self.fileType)

    def guessFileType(self):
      mimeType = magic.from_file(self.path, mime=True)
      return mimeType.split("/")[1]

    def reloadFileType(self):
      oldPath = self.path
      self.fileType = self.guessFileType()
      self.save()

      os.rename(oldPath, self.path)


class UploadSession(models.Model):
    file = models.ForeignKey("TranscodeFile")
    startDate = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(default=0)
    receivedBytes = models.IntegerField(default=0)
    uuid = models.CharField(default=generate_uuid4, max_length=32)

    @property
    def size(self):
      return self.file.size

    @property
    def remainingBytes(self):
      return self.size - self.receivedBytes
