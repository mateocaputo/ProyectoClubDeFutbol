from django.urls import path
from club.views import *

urlpatterns = [
    path("", index, name = "index"),
    path("jugadores", crearJugador, name = "jugadores_form"),
    path("jugadores_busqueda", listar_jugadores, name = "jugadores_list"),
    path("jugadores/<int:dni>/eliminado", eliminar_jugador, name = "eliminar_jugador"),
    path("jugadores/<int:dni>/modificado", modificar_jugador, name = "modificar_jugador"),

    path("patrocinadores_busqueda", listar_patrocinadores, name = "patrocinadores_list"),
    path("patrocinadores", crearPatrocinador, name = "patrocinadores_form"),
    path("patrocinador/<int:numero_interno>/eliminado", eliminar_patrocinador, name = "eliminar_patrocinador"),
    path("patrocinador/<int:numero_interno>/modificado", modificar_patrocinador, name = "modificar_patrocinador"),
    
    path("mobiliario_busqueda", listar_mobiliario, name = "mobiliario_list"),
    path("mobiliario", crearMobiliario, name = "mobiliarios_form"),
    path("mobiliario/<int:numero_serie>/eliminado", eliminar_item, name = "eliminar_item"),
    path("mobiliario/<int:numero_serie>/modificado", modificar_item, name = "modificar_item"),
]
