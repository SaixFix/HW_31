from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ads.models import Categories


def hello(request):
    return JsonResponse({"status": "ok"}, safe=False)


@csrf_exempt
class CategoriesView(View):
    def get(self, request):
        categories = Categories.objects.all()
