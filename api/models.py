from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_type = models.CharField(max_length=128)


class Book(models.Model):
    title = models.CharField(max_length=256)
    genre = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
