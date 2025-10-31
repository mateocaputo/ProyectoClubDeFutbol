from django.contrib import admin
from reservas.models import *
# Register your models here.

admin.site.register(Cancha)
admin.site.register(Medico)

#@admin.register(Cancha)
#class CanchaAdmin(admin.ModelAdmin):
#    list_display = ("nro_cancha", "tipo", "descripcion")
#    list_display_links = ("nro_cancha",)
#    search_fields = ("tipo",)
#    ordering = ("nro_cancha",)