from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from empresas.models import Empresa


class EmpresaSerializer(ModelSerializer):

    class Meta:
        model = Empresa
        fields = ['id', 'empresa', 'descricao']

        read_only_fields = ['id']

