from django.contrib import admin  # type: ignore
from .models import PlatosTipicosDeEcuador

class PlatosTipicosDeEcuadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'region', 'precio')
    search_fields = ('nombre', 'region')
    list_filter = ('region',)

admin.site.register(PlatosTipicosDeEcuador, PlatosTipicosDeEcuadorAdmin)
