from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import *

class CustomUser(AbstractUser):
    email = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200)
    TYPE_CAST = (
    ("admin", "admin"),
    ("user", "user"),
    )
    cast = models.CharField(max_length=6,choices=TYPE_CAST,default="user")
    created_at = models.DateField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
