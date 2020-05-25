from django.db import models

# Create your models here.
class Temp(models.Model):
    title = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    img = models.CharField(max_length=100)

