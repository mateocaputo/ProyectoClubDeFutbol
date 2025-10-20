from django.contrib import admin
from club.models import *

@admin.register(Jugadores)
class JugadoresAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "dni", "dorsal")
    list_display_links = ("dni",)
    search_fields = ("dni", "apellido")
    ordering = ("apellido", "nombre")
    
@admin.register(Patrocinadores)
class PatrocinadoresAdmin(admin.ModelAdmin):
    list_display = ("nombre", "numero_interno")
    list_display_links = ("numero_interno",)
    search_fields = ("numero_interno","nombre")
    ordering = ("numero_interno", "nombre")
    
@admin.register(Mobiliario)
class MobiliarioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cantidad", "marca")
    list_display_links = ("nombre",)
    search_fields = ("marca","nombre")
    ordering = ("nombre",)
