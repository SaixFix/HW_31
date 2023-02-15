import json

from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from ads.models import Category, Ad
from ads.serializers import CategorySerializer, AdDetailSerializer, AdListSerializer
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


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad_data = json.loads(request.body)
        # получаем обьекты класса по заданному полю или 404
        author_id = get_object_or_404(User, pk=ad_data["author_id"])
        category_id = get_object_or_404(Category, pk=ad_data["category_id"])

        ad = Ad.objects.create(
            name=ad_data["name"],
            author_id=author_id,
            price=ad_data["price"],
            description=ad_data["description"],
            is_published=ad_data["is_published"],
            category_id=category_id,
        )

        return JsonResponse({
            "id": ad.id,
            'name': ad.name,
            "author_id": ad.author_id.username,
            "price": ad.price,
            "description": ad.object.description,
            "is_published": ad.object.is_published,
            "category_id": ad.category_id.name,
            "image": ad.image.url if ad.object.image else None
        })


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


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = '__all__'

    def patch(self, request, *args, **kwargs):
        super().post(self, request, *args, **kwargs)
        ad_data = json.loads(request.body)
        # получаем обьекты класса по заданному полю или 404
        author_id = get_object_or_404(User, pk=ad_data["author_id"])

        if 'name' in ad_data:
            self.object.name = ad_data['name']
        if 'price' in ad_data:
            self.object.price = ad_data['price']
        if 'description' in ad_data:
            self.object.description = ad_data['description']
        if 'author_id' in ad_data:
            self.object.author_id = author_id
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


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        ad = self.get_object()
        super().delete(self, request, *args, **kwargs)

        return JsonResponse({
            "id": ad.pk
        })
