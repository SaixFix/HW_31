from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView

from ads.models import Categories, ADS


def hello(request):
    return JsonResponse({"status": "ok"}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesListView(ListView):
    model = Categories

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []
        for category in self.object_list:
            response.append({
                "id": category.id,
                'name': category.name
            })
        return JsonResponse(response, safe=False)


class CategoriesDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object = self.get_object()

        return JsonResponse({
            "id": self.object.id,
            'name': self.object.name
        })


class AdListView(ListView):
    model = ADS

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []
        for ad in self.object_list:
            response.append({
                "id": ad.id,
                'name': ad.name,
                "author": ad.author,
                "price": ad.price
            })
        return JsonResponse(response, safe=False)


class AdDetailView(DetailView):
    model = ADS

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object = self.get_object()

        return JsonResponse({
            "id": self.object.id,
            'name': self.object.name,
            "author": self.object.author,
            "price": self.object.price
        })
