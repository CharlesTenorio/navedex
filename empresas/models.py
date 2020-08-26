from django.db import models

class Empresa(models.Model):
    empresa = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.empresa
