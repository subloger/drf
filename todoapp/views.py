
from rest_framework.viewsets import ModelViewSet
from  rest_framework.pagination import LimitOffsetPagination
from .filters import ProjectFilter, ToDoFilter

from .models import Project, ToDo
from .serializers import ProjectModelSerializer, ToDoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ProjectsPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectAPIView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectsPagination
    filterset_class = ProjectFilter


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer


class ToDoPagination(LimitOffsetPagination):
    default_limit = 20


class ToDoAPIView(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoPagination
    filterset_class = ToDoFilter
