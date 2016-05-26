from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # first_name, last_name and username, password, email are already defined
    # in AbstractUser
    birthdate = models.DateTimeField(default=None, blank=True, null=True)
