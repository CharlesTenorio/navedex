from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from projetos.models import Projeto


class ProjetoSerializer(ModelSerializer):

    class Meta:
        model = Projeto
        fields = ['id', 'id_emrpesa', 'id_nevedex', 'id_cargos', 'projeto', 'inicio_projeto',
                  'fim_projeto', 'descricao' ]

        read_only_fields = ['id']

