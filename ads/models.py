from django.contrib.auth.models import User
from django.db import models


class AD(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=2000)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)


class Category(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=2000)







