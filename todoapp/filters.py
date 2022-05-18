from django_filters import rest_framework as filters
from .models import Project, ToDo


class ProjectFilter(filters.FilterSet):
    project_name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['project_name', 'users_of_project']


class ToDoFilter(filters.FilterSet):
    project = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = ToDo
        fields = ['project']