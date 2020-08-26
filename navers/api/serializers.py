from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from navers.models import Navedex


class NavedexSerializer(ModelSerializer):

    class Meta:
        model = Navedex
        fields = ['id', 'id_usuario', 'nome', 'data_nascimento', 'sexo', 'fone', 'foto_perfil', 'data_cadastro']

        read_only_fields = ['id', 'data_cadastro']

