import pytest

from ads.models import Ad
from ads.serializers.ad import AdCreateSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_create_selection(client, user_token, user):
    """тест на создание выборки"""
    ad_list = AdFactory.create_batch(5)
    data = {
        "slug": "sib111",
        "name": "selection_name",
        "author_id": user.pk,
        "ads": [ad.pk for ad in ad_list]
    }

    expected_response = {
        "id": 1,
        "slug": "sib111",
        "name": "selection_name",
        "author_id": user.pk,
        "ads": [ad.pk for ad in ad_list]
    }

    response = client.post('/selection/create/', data, HTTP_AUTHORIZATION='Bearer ' + user_token)

    assert response.status_code == 201
    assert response.data == expected_response
