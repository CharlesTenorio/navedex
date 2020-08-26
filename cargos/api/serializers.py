from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from cargos.models import Cargo

class CargoSerializer(ModelSerializer):

    class Meta:
        model = Cargo
        fields = ['id', 'cargo']

        read_only_fields = ['id']

