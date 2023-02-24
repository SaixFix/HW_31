import factory.django

from ads.models import Ad, Category
from users.models import User, Location


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    slug = factory.Faker('ean', length=8)
    name = factory.Faker('name')


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location

    slug = 'test'
    name = 'test_location'


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    password = 'testpassword'
    age = 12
    email = factory.Faker('email')


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    slug = factory.Faker('ean', length=8)
    name = factory.Faker('name')
    author_id = factory.SubFactory(UserFactory)
    category_id = factory.SubFactory(CategoryFactory)
    price = 1200
    description = ''
