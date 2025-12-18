from rest_framework import generics, permissions
from .serializers import UsuarioSerializer, RegisterSerializer
from .models import Usuario

class RegisterView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

class UserListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
