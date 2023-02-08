import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Category, AD
from users.models import User


def hello(request):
    return JsonResponse({"status": "ok"}, safe=False)


class CategoriesListView(ListView):
    model = Category
    queryset = Category.objects.order_by('name')

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        categories = self.object_list
        response = []
        for category in categories:
            response.append({
                'id': category.id,
                'name': category.name
            })

        return JsonResponse(response, safe=False)


class CategoriesDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object = self.get_object()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesCreateView(CreateView):
    model = Category
    fields = ['slug', 'name']

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)

        category = Category.objects.create(name=category_data["name"])

        return JsonResponse({
            "id": category.id,
            'name': category.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesUpdateView(UpdateView):
    model = Category
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(self, request, *args, **kwargs)
        category_data = json.loads(request.body)

        self.object.name = category_data['name']
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            'name': self.object.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        cat = self.get_object()
        super().delete(self, request, *args, **kwargs)

        return JsonResponse({
            "id": cat.pk
        })


class AdListView(ListView):
    model = AD
    queryset = AD.objects.order_by('-price')

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        ads = self.object_list
        response = []
        for ad in ads:
            response.append({
                "id": ad.id,
                'name': ad.name,
                "author_id": ad.author_id.username,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "category_id": ad.category_id.name,
                "image": ad.image.url if ad.image else None

            })

        return JsonResponse(response, safe=False)


class AdDetailView(DetailView):
    model = AD

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object = self.get_object()

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
class AdCreateView(CreateView):
    model = AD
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad_data = json.loads(request.body)

        ad = AD.objects.create(
            name=ad_data["name"],
            author_id=get_object_or_404(User, pk=ad_data["author_id"]),
            price=ad_data["price"],
            description=ad_data["description"],
            is_published=ad_data["is_published"],
            category_id=get_object_or_404(Category, pk=ad_data["category_id"]),
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
    model = AD
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
    model = AD
    fields = '__all__'

    def patch(self, request, *args, **kwargs):
        super().post(self, request, *args, **kwargs)
        ad_data = json.loads(request.body)
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
    model = AD
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        ad = self.get_object()
        super().delete(self, request, *args, **kwargs)

        return JsonResponse({
            "id": ad.pk
        })
