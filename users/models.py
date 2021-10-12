from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    administrador = models.BooleanField(default=False)
