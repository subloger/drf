from django.urls import path
from .views import UserListAPIView2

app_name = 'usersapp'
urlpatterns = [
    path('', UserListAPIView2.as_view()),
]
