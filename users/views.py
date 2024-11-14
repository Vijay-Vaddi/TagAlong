"""Views for the user API"""
from rest_framework import generics, authentication, permissions
from users.serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class CreateUserView(generics.CreateAPIView):
    """Create a user in the system"""
    serializer_class = UserSerializer

class UpdateUserView(generics.RetrieveUpdateAPIView):
    """Update a user in the system"""
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user
