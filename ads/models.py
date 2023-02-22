from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


class Category(models.Model):
    slug = models.SlugField(max_length=10, validators=[MinLengthValidator(5)])
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ad(models.Model):
    slug = models.SlugField(max_length=10)
    name = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    author_id = models.ForeignKey("users.User", on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.CharField(max_length=2000, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category_id = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name

    @property
    def author_name(self):
        """возвращает поля username из свянанной модели"""
        return self.author_id.username

    @property
    def cat_name(self):
        """возвращает поля name из свянанной модели"""
        return self.category_id.name


class Selection(models.Model):
    slug = models.SlugField(max_length=10, validators=[MinLengthValidator(5)])
    name = models.CharField(max_length=50)
    author_id = models.ForeignKey("users.User", on_delete=models.CASCADE)
    ads = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def __str__(self):
        return self.name















