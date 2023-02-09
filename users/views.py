import json

from django.conf import settings
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from users.models import User, Location


class UserListView(ListView):
    model = User
    #queryset с параметрами подсчета ad__is_published и сортировкой по юзернейму
    queryset = User.objects.annotate(total_ads=Count("ad", filter=Q(ad__is_published=True))).order_by("username")

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        # Пагинация
        paginator = Paginator(self.object_list, settings.OBJECT_ON_PAGE)
        page_num = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_num)

        users = []

        for user in page_obj:
            users.append({
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "role": user.role,
                "age": user.age,
                "locations": [loc.name for loc in user.locations.all()],
                "total_ads": user.total_ads
            })

        response = {
            "items": users,
            "num_pages": paginator.num_pages,
            "total": paginator.count

        }

        return JsonResponse(response, safe=False)


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object = self.get_object()

        return JsonResponse({
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            "username": self.object.username,
            "role": self.object.role,
            "age": self.object.age,
            "locations": [loc.name for loc in self.object.locations.all()],
            "total_ads": self.object.ad_set.filter(is_published=True).count()
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ['__all__']

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)

        user = User.objects.create(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            username=user_data["username"],
            password=user_data["password"],
            role=user_data["role"],
            age=user_data["age"],
        )

        for loc in user_data.get("locations"):
            # создаем новую локацию если такой еще нет
            location, _ = Location.objects.get_or_create(name=loc)
            user.locations.add(location)

        return JsonResponse({
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "role": user.role,
            "age": user.age,
            "locations": [loc.name for loc in user.locations.all()],
            "total_ads": user.ad_set.filter(is_published=True).count()
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ['username']

    def patch(self, request, *args, **kwargs):
        super().post(self, request, *args, **kwargs)
        user_data = json.loads(request.body)

        if "username" in user_data:
            self.object.username = user_data['username']
        if "first_name" in user_data:
            self.object.first_name = user_data["first_name"]
        if "last_name" in user_data:
            self.object.last_name = user_data["last_name"]
        if "password" in user_data:
            self.object.password = user_data["password"]
        if "role" in user_data:
            self.object.role = user_data["role"]
        if "age" in user_data:
            self.object.age = user_data["age"]
        if "locations" in user_data:
            #удаляем существующие локации
            self.object.locations.all().delete()
            # создаем новую локацию если такой еще нет
            for loc in user_data.get("locations"):
                location, _ = Location.objects.get_or_create(name=loc)
                self.object.locations.add(location)

        self.object.save()

        return JsonResponse({
            "username": self.object.username,
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            "role": self.object.role,
            "age": self.object.age,
            "locations": [loc.name for loc in self.object.locations.all()]
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        super().delete(self, request, *args, **kwargs)

        return JsonResponse({
            "id": user.pk
        })
