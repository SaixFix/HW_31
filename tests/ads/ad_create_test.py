import pytest

from ads.models import Ad
from ads.serializers.ad import AdCreateSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_create_ad(client, user_token, user, category):
    """тест на создание объявления"""
    data = {
        "slug": "sib1",
        "name": "Сибирская 12",
        "price": 10,
        "description": "",
        "author_id": user.pk,
        "category_id": category.pk
    }

    expected_response = {
        "id": 1,
        "image": None,
        "is_published": False,
        "slug": "sib1",
        "name": "Сибирская 12",
        "price": 10,
        "description": "",
        "author_id": user.pk,
        "category_id": category.pk
    }

    response = client.post('/ad/create/', data, HTTP_AUTHORIZATION='Bearer ' + user_token)

    assert response.status_code == 201
    assert response.data == expected_response
