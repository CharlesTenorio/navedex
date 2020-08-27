from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from cargos.models import Cargo
from .serializers import CargoSerializer


class CargoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('cargo',)
