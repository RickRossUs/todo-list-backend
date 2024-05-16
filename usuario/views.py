from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .serializers import UsuarioSerializer

class IsSelfOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsSelfOrReadOnly()]
        else:
            return [permissions.IsAuthenticated()]
        
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return get_user_model().objects.filter(id=self.request.user.id)
        else:
            return get_user_model().objects.none()
