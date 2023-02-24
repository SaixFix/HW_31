import pytest

from ads.serializers.ad import AdDetailSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_detail(client, user_token):
    "Тест на получения обьявления по id"
    ad = AdFactory.create()

    expected_response = AdDetailSerializer(ad).data

    response = client.get(f'/ad/{ad.pk}/', HTTP_AUTHORIZATION='Bearer ' + user_token)

    assert response.status_code == 200
    assert response.data == expected_response
