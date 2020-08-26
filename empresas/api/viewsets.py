from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from empresas.models import Empresa
from .serializers import EmpresaSerializer


class EmpesaViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('empresa',)
