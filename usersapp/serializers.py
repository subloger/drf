from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.serializers import ModelSerializer
# from django.contrib.auth.models import User
from .models import User


class UserModelSerializer(ModelSerializer):
# class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        #fields = '__all__'
        exclude = ['uid', 'is_superuser', 'is_staff']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff')
