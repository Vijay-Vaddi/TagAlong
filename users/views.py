"""Views for the user API"""
from rest_framework import generics
from users.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    """Create a user in the system"""
    serializer_class = UserSerializer

class UpdateUserView(generics.UpdateAPIView):
    """Update a user in the system"""
    serializer_class = UserSerializer
