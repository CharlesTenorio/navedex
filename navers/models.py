from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Navedex(models.Model):
    id_usuario = models.OneToOneField(
        User, verbose_name=("Usuario"), on_delete=models.PROTECT)
    nome = models.CharField(max_length=80, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    fone = models.CharField(max_length=15, blank=True, null=True)
    foto_perfil = models.FileField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_created=True, blank=True, null=True)

    def __str__(self):
        return self.nome

