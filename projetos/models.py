from django.db import models
from empresas.models import Empresa
from navers.models import Navedex
from cargos.models import Cargo


class Projeto(models.Model):
    id_emrpesa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    id_nevedex= models.ForeignKey(Navedex, on_delete=models.PROTECT)
    id_cargos = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    projeto = models.CharField(max_length=80)
    inicio_projeto = models.DateField()
    fim_projeto = models.DateField()
    descricao = models.TextField(max_length=1000)

    def __str__(self):
        return self.projeto
