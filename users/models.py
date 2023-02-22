from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.validators import check_email_blacklist


class Location(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=100, unique=True)
    # max_digits цифры перед запятой, decimal_places после запятой
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Дислокация'
        verbose_name_plural = 'Дислокации'

    def __str__(self):
        return self.name


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member') #1 значение в базу, 2 для отображения
    MODERATOR = 'moderator', _('moderator')
    ADMIN = 'admin', _('admin')


class User(AbstractUser):
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(9)])
    locations = models.ManyToManyField(Location)
    email = models.EmailField(unique=True, validators=[check_email_blacklist])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username






