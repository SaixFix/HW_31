from django.urls import path

from ads.views import *

urlpatterns = [
    path('hello/', hello, name='get_list_categories'),
    path('', CategoriesListView.as_view(), name='get_list_categories'),
    path('<int:pk>/', CategoriesDetailView.as_view(), name='get_one_categories'),
    path('create/', CategoriesCreateView.as_view(), name='create_categories'),
    path('<int:pk>/update/', CategoriesUpdateView.as_view(), name='update_categories'),
    path('<int:pk>/delete/', CategoriesDeleteView.as_view(), name='delete_categories'),
    path('ad/', AdView.as_view()),
    path('ad/<int:pk>/', AdDetailView.as_view())
]