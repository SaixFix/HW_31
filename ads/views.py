from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from ads.models import Category, Ad
from ads.serializers import CategorySerializer, AdDetailSerializer, AdListSerializer, AdCreateSerializer, \
    AdUpdateSerializer, AdDestroySerializer, AdUploadImageSerializer


def hello(request):
    return JsonResponse({"status": "ok"}, safe=False)


class CategoryViewSet(ModelViewSet):
    """"ViewSet с полным CRUD"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AdListView(ListAPIView):
    queryset = Ad.objects.order_by('-price')
    serializer_class = AdListSerializer

    def get(self, request, *args, **kwargs):
        """Функция для обработки запросов"""

        # Функция поиска обьявлений по category_id
        category_id = request.GET.get('cat', None)
        if category_id:
            self.queryset = self.queryset.filter(
                category_id__pk__exact=category_id
            )

        # Функция поиска обьявлений по вхождению слова в названиях
        name_text = request.GET.get('text', None)
        if name_text:
            self.queryset = self.queryset.filter(
                name__icontains=name_text
            )

        # Функция поиска обьявлений по локации
        location = request.GET.get('location', None)
        if name_text:
            self.queryset = self.queryset.filter(
                author_id__locations__icontains=location
            )

        # Функция поиска обьявлений по диапазону цены
        price_from = request.GET.get('price_from', None)
        price_to = request.GET.get('price_to', None)
        if price_from and price_to:
            self.queryset = self.queryset.filter(
                price__gte=price_from,
                price__lte=price_to
            )

        return super().get(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


class AdUploadImage(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUploadImageSerializer

    def update(self, request, *args, **kwargs):
        """функция загрузки изображений в модели AD"""
        self.object = self.get_object()
        self.object.image = request.FILES.get('image')

        return super().update(request, *args, **kwargs)


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDestroySerializer
