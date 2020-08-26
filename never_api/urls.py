from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from usuarios.api.views import registra_view, CustomAuthToken, MyTokenObtainPairView
from cargos.api.viewsets import CargoViewSet
from empresas.api.viewsets import EmpesaViewSet
from navers.api.viewsets import NavedexViewSet
from projetos.api.viewsets import ProjetoViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Navedex API",
      default_version='v1',
      description="Documentacao APIS",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
router = routers.SimpleRouter()
router.register(r'api/cargos/cargo', CargoViewSet)
router.register(r'api/empresas/empresa', EmpesaViewSet)
router.register(r'api/navedexs/navedex', NavedexViewSet)
router.register(r'api/projetos/projeto', ProjetoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/usr/registra_usr/', registra_view, name='registrar'),
    path('api/api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('api/usr/obeter_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/usr/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/usr/jwt/', MyTokenObtainPairView.as_view(), name='token_refresh'),

]
