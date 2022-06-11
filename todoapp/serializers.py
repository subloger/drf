from rest_framework import serializers
from .models import Project, ToDo


class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # fields = '__all__'
        exclude = ['repo_link']

    # def validate(self, attrs):
    #     print("a" * 60)
    #     print(attrs)
    #     return attrs


class ToDoModelSerializer(serializers.HyperlinkedModelSerializer):
    project = ProjectModelSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'
