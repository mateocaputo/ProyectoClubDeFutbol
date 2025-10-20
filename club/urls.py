from django.urls import path
from club.views import *

urlpatterns = [
    path("", index, name = "index"),
    path("jugadores", crearJugador, name = "jugadores_form"),
    path("jugadores_busqueda", listar_jugadores, name = "jugadores_list"),
    path("patrocinadores_busqueda", listar_patrocinadores, name = "patrocinadores_list"),
    path("mobiliario_busqueda", listar_mobiliario, name = "mobiliario_list"),
    path("patrocinadores", crearPatrocinador, name = "patrocinadores_form"),
    path("mobiliario", crearMobiliario, name = "mobiliarios_form"),
]
