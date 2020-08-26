from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from projetos.models import Projeto
from .serializers import ProjetoSerializer


class ProjetoViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Projeto.objects.all()
    serializer_class = Projeto
    filter_backends = (SearchFilter,)
    search_fields = ('projeto',)
