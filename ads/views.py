import json

from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from ads.models import Category, Ad
from ads.serializers import CategorySerializer, AdDetailSerializer, AdListSerializer, AdCreateSerializer, \
    AdUpdateSerializer, AdDestroySerializer
from users.models import User


def hello(request):
    return JsonResponse({"status": "ok"}, safe=False)


class CategoryViewSet(ModelViewSet):
    """"ViewSet с полным CRUD"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AdListView(ListAPIView):
    queryset = Ad.objects.order_by('-price')
    serializer_class = AdListSerializer


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImage(UpdateView):
    model = Ad
    fields = "image"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES.get('image')
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            'name': self.object.name,
            "author_id": self.object.author_id.username,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category_id": self.object.category_id.name,
            "image": self.object.image.url if self.object.image else None
        })


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDestroySerializer
