from django.db import models


class ADS(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=2000)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)


class Categories(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=2000)
