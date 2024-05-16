from rest_framework import serializers
from django.contrib.auth import get_user_model

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = "__all__"

    def create(self, validated_data):
        user = get_user_model()(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
