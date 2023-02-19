from django.db.models import Q, Count
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from users.models import User, Location
from users.permissions import UserPersonalPermission, ReadOnly
from users.serializers import UserListSerializer, UserDetailSerializer, UserCreateSerializer, UserDestroySerializer, \
    UserUpdateSerializer, LocationSerializer


class LocationViewSet(ModelViewSet):
    """"ViewSet с полным CRUD"""
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAdminUser | ReadOnly]


class UserListView(ListAPIView):
    # queryset с параметрами подсчета ad__is_published и сортировкой по юзернейму
    queryset = User.objects.annotate(total_ads=Count("ad", filter=Q(ad__is_published=True))).order_by("username")
    serializer_class = UserListSerializer
    permission_classes = [IsAdminUser]


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.annotate(total_ads=Count("ad", filter=Q(ad__is_published=True)))
    serializer_class = UserDetailSerializer
    permission_classes = [UserPersonalPermission | IsAdminUser]


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [UserPersonalPermission | IsAdminUser]


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer
    permission_classes = [UserPersonalPermission | IsAdminUser]
