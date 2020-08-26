from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
import json
from rest_framework.views import APIView
from usuarios.views import UsuariosSistema

User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.first_name
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'name': user.get_full_name()
        })


@api_view(['POST', ])
def registra_view(request):
    '''Passa os paramentroes email,  password e first_name '''

    email = request.POST.get('email', '')
    queryset = User.objects.filter(email=email)
    if queryset.exists():
        user = queryset.first()
        token, created = Token.objects.get_or_create(user=user)
        data = UserSerializer(user).data
        data['token'] = token.key
        if hasattr(user, 'cliente'):
            return Response({'detail': 'Esse email já existe', 'error': True}, status=status.HTTP_409_CONFLICT)
        return Response(data, status=200)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        data = serializer.data
        data['token'] = token.key
        return Response(data, status=201)
    return Response(serializer.errors)



@api_view(['POST',])
def login(request, data=None):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    user_type = request.POST.get('type', 'cliente')
    if not email:
        return Response({'detail': 'email é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)
    elif not password:
        return Response({'detail': 'password é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(email=email).first()
    if user and user.check_password(password):
        if hasattr(user, user_type):
            token, created = Token.objects.get_or_create(user=user)
            data['token'] = token.key
            return Response(data, status=200)
    return Response({'detail': 'usuario ou senha inválidos'}, status=404)
