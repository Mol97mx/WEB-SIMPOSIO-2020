from django.contrib import admin
from .models import registro
# Register your models here.

class registroAdmin(admin.ModelAdmin):
    readonly_fields=('fechaderegistro','fechademodificacion')
    list_display = ('nombre','apellidop','apellidom','email','opcion')
    ordering = ('nombre','apellidop','apellidom')
    search_fields=('nombre','apellidop','apellidom','email')
    list_filter=('nombre','apellidop','email','opcion')

admin.site.register(registro,registroAdmin)