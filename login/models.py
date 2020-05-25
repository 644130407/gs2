from datetime import datetime

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=64)
    birthday = models.DateField()
    email = models.EmailField(default="")
    thumb = models.CharField(max_length=100, default="")
    gender = models.IntegerField(default=1)
    hobby = models.CharField(max_length=100)
    pos = models.IntegerField(default=1)
    # user = models.OneToOneField(Users, on_delete=models.CASCADE)

class Users(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=256)
    userinfo = models.OneToOneField(UserInfo, on_delete=models.CASCADE)

