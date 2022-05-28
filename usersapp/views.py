from rest_framework.renderers import JSONRenderer
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserListAPIView(ModelViewSet):
    # renderer_classes = [JSONRenderer]
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
