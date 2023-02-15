from django.urls import path

from users.views import UserListView, UserDetailView, UserCreateView, UserDeleteView, UserUpdateView, LocationViewSet


urlpatterns = [
    path('', UserListView.as_view(), name="users_list"),
    path('<int:pk>/', UserDetailView.as_view(), name='get_user_detail'),
    path('create/', UserCreateView.as_view(), name='create_user'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update_user'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete_user'),
]
