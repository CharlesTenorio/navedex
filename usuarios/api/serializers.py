from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from usuarios.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        user = super().save()
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class UserGetSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']
