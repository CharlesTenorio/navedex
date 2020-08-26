from django.contrib import admin
from .models import Navedex


class NavedexAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_usuario', 'nome', 'data_nascimento', 'sexo', 'fone', 'foto_perfil', 'data_cadastro' )
    search_fields = ('nome',)

admin.site.register(Navedex, Navedex)
