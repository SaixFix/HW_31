import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, AD


def hello(request):
    return JsonResponse({"status": "ok"}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    def get(self, request):
        categories = Categories.objects.all()
        response = []
        for category in categories:
            response.append({
                "id": category.id,
                'name': category.name
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        category_data = json.loads(request.body)

        category = Categories()
        category.name = category_data["name"]

        category.save()

        return JsonResponse({
                "id": category.id,
                'name': category.name
            })


class CategoriesDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object = self.get_object()

        return JsonResponse({
            "id": self.object.id,
            'name': self.object.name
        })


class AdView(View):

    def get(self, request):
        ads = AD.objects.all()
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

        ad = ADS()
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
