from django.db import models

# Create your models here.
from login.models import Users




class ArticleType(models.Model):
    title = models.CharField(max_length=256, unique=True)
    sort = models.IntegerField(default=0)
class Column(models.Model):
    title = models.CharField(max_length=64, default='')
    sort = models.IntegerField(default=0)
    template = models.IntegerField(default=1)
    articleType = models.ForeignKey(ArticleType, on_delete=models.CASCADE)
class BackImg(models.Model):
    url = models.CharField(max_length=100)
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
class Content(models.Model):
    title = models.CharField(max_length=64, default='')
    content = models.CharField(max_length=1024, null=True)
    column = models.ForeignKey(Column, on_delete=models.CASCADE, default='')

    sort = models.IntegerField(default=0)


class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=10240)

    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    type = models.ForeignKey(ArticleType, on_delete=models.CASCADE)
