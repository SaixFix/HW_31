from django.urls import path

from ads.views.selection import *

urlpatterns = [
    path('', SelectionListView.as_view(), name='selection_get_list'),
    path('<int:pk>/', SelectionDetailView.as_view(), name='selection_detail'),
    path('create/', SelectionCreateView.as_view(), name='selection_create'),
    path('<int:pk>/update/', SelectionUpdateView.as_view(), name='selection_update'),
    path('<int:pk>/delete/', SelectionDeleteView.as_view(), name='selection_delete'),
]
