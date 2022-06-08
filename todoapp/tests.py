import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from django.contrib.auth.models import User
from .views import ProjectAPIView, ToDoAPIView
from .models import Project, ToDo


class TestProjectAPIView(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects/')
        view = ProjectAPIView.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/projects/', {'project_name': 'Project_5',
                                                  'repo_link': 'https://any.com',
                                                  'users_of_project': 'user_1'}, format='json')
        view = ProjectAPIView.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_detail(self):
        project = Project.objects.create(project_name='Project_5',
                                         repo_link='https://any.com')
        client = APIClient()
        response = client.get(f'/api/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        project = Project.objects.create(project_name='Project_5',
                                         repo_link='https://any.com')
        client = APIClient()
        response = client.put(f'/api/projects/{project.id}/', {'project_name': 'Project_6',
                                                               'repo_link': 'https://any.com'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestToDoAPIView(APITestCase):

    def test_get_list(self):
        response = self.client.get('/api/todo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        project = Project.objects.create(project_name='Project_6', repo_link='https://any.com')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'/api/projects/{project.id}/', {'project_name': 'Project_7',
                                                                    'repo_link': 'https://any.com'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(project.project_name, 'Project_7')
