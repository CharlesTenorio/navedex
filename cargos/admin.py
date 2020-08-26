from django.contrib import admin
from .models import Cargo

class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cargo')
    search_fields = ('cargo',)


admin.site.register(Cargo, CargoAdmin)
