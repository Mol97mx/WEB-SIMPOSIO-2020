from django.contrib import admin
from .models import Galeria
# Register your models here.

class GaleriaAdmin(admin.ModelAdmin):
    readonly_fields=('creado','actualizado')
    list_display = ('titulo','autor')
    ordering = ('autor','titulo')
    search_fields=('titulo','descripcion','autor__username')
    list_filter=('autor__username',)

admin.site.register(Galeria, GaleriaAdmin) 