"""usertodo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from usersapp.views import UserModelViewSet, UserListAPIView
from todoapp.views import ProjectModelViewSet, ToDoModelViewSet
from todoapp.views import ProjectAPIView, ToDoAPIView

schema_view = get_schema_view(
    openapi.Info(
        title='User-TODO',
        default_version='1',
        description='Documentation for project',
        contact=openapi.Contact(email='admin@admin.com'),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('users', UserListAPIView)
router.register('projects', ProjectAPIView)
router.register('todo', ToDoAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('todo/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/users/1', include('usersapp.urls', namespace='1')),
    path('api/users/2', include('usersapp.urls', namespace='2')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
