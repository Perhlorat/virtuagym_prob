from django.contrib.auth.models import User
from rest_framework import viewsets

from users.serializers import UserSerializer


class UserViewset(viewsets.ModelViewSet):
    """
    Simple restaurant REST API CRUD ViewSet
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
