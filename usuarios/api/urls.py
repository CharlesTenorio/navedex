from django.urls import path
from usuarios.api.views import registra_view, login

urlpatterns = [
    path('usuario/registrar/', registra_view),
    path('usuario/login/', login),

]
