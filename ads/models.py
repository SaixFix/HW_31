from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=100, unique=True)
    # max_digits цифры перед запятой, decimal_places после запятой
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)


class Category(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class UserRoles(models.TextChoices):
    MEMBER = 'MB', _('member') #1 значение в базу, 2 для отображения
    MODERATOR = "MD", _('moderator')
    ADMIN = "AD", _('admin')


class User(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=10, unique=True)
    role = models.CharField(max_length=2, choices=UserRoles.choices)
    age = models.PositiveSmallIntegerField()
    location_id = models.ForeignKey(Location, models.CASCADE)


class AD(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=200)
    author_id = models.ForeignKey('User', on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'















