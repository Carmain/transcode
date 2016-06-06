import uuid
import magic
import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

TYPES_TABLE = {
    "audio/mpeg": "mp3"
}


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


class TranscodeFile(FileMixin, models.Model):
    owner = models.ForeignKey("User", default=None, null=True, blank=True)
    uuid = models.CharField(default=generate_uuid4, max_length=32)
    fileType = models.CharField(choices=settings.SUPPORTED_FILES, default="tmp", max_length=5)
    size = models.IntegerField()

    def guessFileType(self):
        print(self.path)
        mimeType = magic.from_file(self.path, mime=True).decode("utf-8")
        if mimeType in TYPES_TABLE:
            return TYPES_TABLE.get(mimeType)
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


class ConvertJob(models.Model):
    state = models.IntegerField(default=0)
    file = models.ForeignKey("TranscodeFile")
    task_uuid = models.CharField(max_length=32)
