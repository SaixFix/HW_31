from django.db import models


class Category(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ad(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=200)
    author_id = models.ForeignKey("users.User", on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
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















