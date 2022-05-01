from rest_framework import serializers
from .models import Project, ToDo


class ProjectModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        # fields = '__all__'
        exclude =['repo_link']


class ToDoModelSerializer(serializers.HyperlinkedModelSerializer):
    project = ProjectModelSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'
