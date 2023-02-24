import pytest


@pytest.fixture
@pytest.mark.django_db
def user_token(client, django_user_model):
    """фикстура для получения токена авторизации"""
    username = 'test_user13'
    password = 'testpassword'
    age = 12
    email = 'test13@mail.ru'

    # создаем пользователя
    django_user_model.objects.create_user(
        username=username,
        password=password,
        age=age,
        email=email
    )

    # авторизовались созданным пользователем
    response = client.post(
        '/user/token/',
        {"username": username, "password": password},
        format='json'

    )

    # забираем токен
    return response.data['access']
