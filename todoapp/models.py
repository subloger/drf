from django.db import models
from usersapp.models import User


class Project(models.Model):
    project_name = models.CharField(max_length=64)
    repo_link = models.URLField(blank=True)
    users_of_project = models.ManyToManyField(User)


class ToDo(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    note_text = models.TextField(max_length=1000)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField()
