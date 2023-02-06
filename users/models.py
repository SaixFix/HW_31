from django.db import models
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=100, unique=True)
    # max_digits цифры перед запятой, decimal_places после запятой
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member') #1 значение в базу, 2 для отображения
    MODERATOR = 'moderator', _('moderator')
    ADMIN = 'admin', _('admin')


class User(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=9, choices=UserRoles.choices)
    age = models.PositiveSmallIntegerField()
    locations = models.ManyToManyField(Location)
