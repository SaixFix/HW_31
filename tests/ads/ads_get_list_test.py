import pytest

from ads.serializers.ad import AdListSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ads_list(client, user_token):
    "Тест на получения списка объявлений"
    ad_list = AdFactory.create_batch(4)

    expected_response = {
        "count": 4,
        "next": None,
        "previous": None,
        "results": AdListSerializer(ad_list, many=True).data
    }

    response = client.get('/ad/', HTTP_AUTHORIZATION='Bearer ' + user_token)

    assert response.status_code == 200
    assert response.data == expected_response
