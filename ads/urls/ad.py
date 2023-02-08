from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from ads.views import *

urlpatterns = [
    path('', AdListView.as_view(), name='get_list_ads'),
    path('<int:pk>/', AdDetailView.as_view(), name='get_ad_detail'),
    path('create/', AdCreateView.as_view(), name='create_categories'),
    path('<int:pk>/upload-image/', AdUploadImage.as_view(), name='ad_upload_image'),
    # path('<int:pk>/update/', AdUpdateView.as_view(), name='update_ad'),
    # path('<int:pk>/delete/', AdDeleteView.as_view(), name='delete_ad'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
