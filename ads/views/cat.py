from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from ads.models import Category
from ads.permissions import ReadOnly
from ads.serializers.cat import CategorySerializer


class CategoryViewSet(ModelViewSet):
    """"ViewSet с полным CRUD"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAdminUser | ReadOnly]