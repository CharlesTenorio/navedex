from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
User = get_user_model()


class UsuarioViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
