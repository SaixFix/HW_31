import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Category, AD


def hello(request):
    return JsonResponse({"status": "ok"}, safe=False)


class CategoriesListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        categories = self.object_list
        response = []
        for category in categories:
            response.append({
                "id": category.id,
                'name': category.name
            })

        return JsonResponse(response, safe=False)


class CategoriesDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object = self.get_object()

        return JsonResponse({
            "id": self.object.id,
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

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        ads = self.object_list()
        response = []
        for ad in ads:
            response.append({
                "id": ad.id,
                'name': ad.name,
                "author": ad.author,
                "price": ad.price
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        ad_data = json.loads(request.body)

        ad = AD()
        ad.name = ad_data["name"]
        ad.author = ad_data["author"]
        ad.price = ad_data["price"]
        ad.description = ad_data["description"]
        ad.address = ad_data["address"]
        ad.is_published = ad_data["is_published"]

        ad.save()

        return JsonResponse({
            "id": ad.id,
            'name': ad.name,
            "author": ad.author,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        })


class AdDetailView(DetailView):
    model = AD

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object = self.get_object()

        return JsonResponse({
            "id": self.object.id,
            'name': self.object.name,
            "author": self.object.author,
            "price": self.object.price
        })
