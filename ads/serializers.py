from rest_framework import serializers

from ads.models import Category, Ad


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'




class AdListSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField()
    category_id = serializers.IntegerField()

    class Meta:
        model = Ad
        field = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField()
    category_id = serializers.IntegerField()

    class Meta:
        model = Ad
        field = '__all__'