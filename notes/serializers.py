from rest_framework import serializers
from .models import Note
from usuario.serializers import UsuarioSerializer

class NoteSerializer(serializers.ModelSerializer):
    user = UsuarioSerializer(read_only=True)
    class Meta:
        model = Note
        fields = "__all__"
