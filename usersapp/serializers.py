from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.serializers import ModelSerializer
from .models import User


class UserModelSerializer(ModelSerializer):
#class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        #exclude = ['uid']
