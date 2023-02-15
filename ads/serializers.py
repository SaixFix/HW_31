from rest_framework import serializers

from ads.models import Category, Ad
from users.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = [
            'name', 'author_id', 'price',
            'is_published', 'category_id'
        ]


class AdDetailSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField()
    cat_name = serializers.CharField()

    class Meta:
        model = Ad
        fields = ['id', 'slug', 'name', 'author_id', 'author_name',
                  'price', 'is_published', 'category_id', 'cat_name'
                  ]
