from django.contrib import admin
from .models import Projeto


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_emrpesa', 'id_nevedex', 'id_cargos', 'projeto', 'inicio_projeto', 'fim_projeto',
                    'descricao' )
    search_fields = ('projeto',)

admin.site.register(Projeto, ProjetoAdmin)

