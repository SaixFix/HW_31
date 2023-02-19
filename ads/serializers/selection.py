from rest_framework import serializers

from ads.models import Selection, Ad
from ads.serializers.ad import AdPartSerializer


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ['id', 'name']


class SelectionDetailSerializer(serializers.ModelSerializer):
    ads = AdPartSerializer(read_only=True, many=True)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = 'id'
