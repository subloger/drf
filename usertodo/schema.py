import graphene
from graphene_django import DjangoObjectType

from todoapp.models import ToDo, Project
from usersapp.models import User


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(graphene.ObjectType):
    all_todo = graphene.List(ToDoType)
    all_projects = graphene.List(ProjectType)
    all_users = graphene.List(UserType)

    def resolve_all_todo(root):
        return ToDo.objects.all()

    def resolve_all_projects(self, root):
        return Project.objects.all()

    def resolve_all_users(self, root):
        return User.objects.all()


schema = graphene.Schema(query=Query)
