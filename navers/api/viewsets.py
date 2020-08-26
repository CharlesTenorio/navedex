from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from navers.models import Navedex
from .serializers import NavedexSerializer


class NavedexViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Navedex.objects.all()
    serializer_class = NavedexSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('Nome',)
