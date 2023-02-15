from django.urls import path

from ads.views import *

urlpatterns = [
    path('hello/', hello, name='get_list_categories'),
]
