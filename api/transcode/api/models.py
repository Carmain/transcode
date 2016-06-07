from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from converter import Converter
import uuid
import os

def generate_uuid4():
    return uuid.uuid4().hex


class FileMixin(object):
    @property
    def fileName(self):
        return "{0}.{1}".format(self.uuid, self.fileType)

    @property
    def path(self):
        return os.path.join(settings.UPLOAD_DIRECTORY, self.fileName)


class User(AbstractUser):
    # first_name, last_name and username, password, email are already defined
    # in AbstractUser
    birthdate = models.DateTimeField(default=None, blank=True, null=True)
    disk_space = models.BigIntegerField(default=1e10)

    @property
    def used_space(self):
        transcode_files = self.transcodefile_set.all()
        used_space = 0

        for file in transcode_files:
            used_space += file.size

        return used_space

    @property
    def free_space(self):
        return self.disk_space - self.used_space


class ConvertedFile(FileMixin, models.Model):
    fileType = models.CharField(choices=settings.SUPPORTED_FILES, max_length=5)
    transcode_file = models.ForeignKey("TranscodeFile")
    date = models.DateTimeField(auto_now_add=True)


class TranscodeFile(FileMixin, models.Model):
    owner = models.ForeignKey("User", default=None, null=True, blank=True)
    uuid = models.CharField(default=generate_uuid4, max_length=32)
    fileType = models.CharField(choices=settings.SUPPORTED_FILES, default="tmp", max_length=5)
    size = models.IntegerField()
    duration = models.FloatField(default=0.0)
    name = models.CharField(max_length=256)

    def fetchMetaDatas(self):
      c = Converter()
      infos = c.probe(self.path)

      if infos is None:
        os.remove(self.path)
        raise TypeError("File is not a valid media.")

      old_path = self.path
      self.duration = infos.streams[0].duration
      self.fileType = infos.format.format
      self.save()
      os.rename(old_path, self.path)

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


class ConvertJob(models.Model):
    state = models.IntegerField(default=0)
    file = models.ForeignKey("TranscodeFile")
    task_uuid = models.CharField(max_length=32)
