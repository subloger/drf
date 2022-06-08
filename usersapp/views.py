from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import User
from .serializers import UserModelSerializer, UserSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserListAPIView(ModelViewSet):
    # renderer_classes = [JSONRenderer]
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserListAPIView2(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.version == '2':
            return UserSerializer
        return UserModelSerializer
