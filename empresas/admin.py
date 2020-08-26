from django.contrib import admin
from .models import Empresa

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'empresa', 'descricao')
    search_fields = ('empresa',)


admin.site.register(Empresa, EmpresaAdmin)

# Register your models here.
