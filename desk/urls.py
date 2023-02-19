from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from ads.views.ad import hello
from ads.views.cat import CategoryViewSet
from users.views import LocationViewSet

router = routers.SimpleRouter()
router.register('cat', CategoryViewSet)
router.register('location', LocationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', hello),
    path('ad/', include('ads.urls.ad')),
    path('user/', include('users.urls')),
    path('selection/', include('ads.urls.selection')),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
