from rest_framework import serializers

from users.models import User, UserRoles, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'lat', 'lng']


class UserListSerializer(serializers.ModelSerializer):
    total_ads = serializers.IntegerField()
    locations = LocationSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = User
        exclude = ['password']


class UserDetailSerializer(serializers.ModelSerializer):
    total_ads = serializers.IntegerField()
    locations = LocationSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = User
        exclude = ['password']


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    locations = LocationSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        """отлючаем выпадение ошибки в случае если принятой локации не существует"""
        self._location = self.initial_data.pop('locations')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        """переопределили метод create для возможности получит или создать локацию"""
        user = User.objects.create(**validated_data)
        # создаем новую локацию если такой еще нет
        location, _ = Location.objects.get_or_create(name=self._location)
        user.locations.add(location)

        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    username = serializers.CharField(required=False)
    role = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    locations = LocationSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, *, raise_exception=False):
        """отлючаем выпадение ошибки в случае если принятой локации не существует"""
        self._location = self.initial_data.pop('locations')
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        """переопределили метод create для возможности получит или создать локацию"""
        user = super().save()
        # создаем новую локацию если такой еще нет
        location, _ = Location.objects.get_or_create(name=self._location)
        user.locations.add(location)

        user.save()
        return user


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id'
