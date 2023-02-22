from rest_framework import serializers

from ads.models import Ad
from ads.validators import check_not_true


class AdPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = [
            'id', 'name', 'author_id', 'price', 'image',
            'is_published', 'category_id', 'description'
        ]


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = [
            'id', 'name', 'author_id', 'price',
            'is_published', 'category_id'
        ]


class AdDetailSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField()
    cat_name = serializers.CharField()

    class Meta:
        model = Ad
        fields = ['id', 'slug', 'name', 'author_id', 'author_name',
                  'price', 'is_published', 'category_id', 'cat_name', 'image'
                  ]


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    image = serializers.ImageField(required=False)
    is_published = serializers.BooleanField(required=False, validators=[check_not_true])

    class Meta:
        model = Ad
        fields = '__all__'


class AdUpdateSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Ad
        fields = [
            'id', 'slug', 'name', 'price', 'author_id',
            'is_published', 'description', 'category_id'
        ]


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id']


class AdUploadImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    image = serializers.ImageField()

    class Meta:
        model = Ad
        fields = ['id', 'name', 'image']