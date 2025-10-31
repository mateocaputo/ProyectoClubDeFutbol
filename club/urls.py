from django.urls import path
from club.views import *

urlpatterns = [
    path("", index, name = "index"),
    path("jugadores", crearJugador, name = "jugadores_form"),
    path("jugadores/busqueda", listar_jugadores, name = "jugadores_list"),
    path("jugadores/<int:dni>/eliminado", eliminar_jugador, name = "eliminar_jugador"),
    path("jugadores/<int:dni>/modificado", modificar_jugador, name = "modificar_jugador"),
    path("jugadores/<int:dni>/jugador_detalle", JugadorDetailView.as_view(), name = "jugador_detail"),


    path("patrocinadores/busqueda", listar_patrocinadores, name = "patrocinadores_list"),
    path("patrocinadores", crearPatrocinador, name = "patrocinadores_form"),
    path("patrocinador/<int:numero_interno>/eliminado", eliminar_patrocinador, name = "eliminar_patrocinador"),
    path("patrocinador/<int:numero_interno>/modificado", modificar_patrocinador, name = "modificar_patrocinador"),
    path("patrocinador/<int:numero_interno>/patrocinador_detalle", PatrocinadorDetailView.as_view(), name = "patrocinador_detail"),
    
    path("mobiliario/busqueda", listar_mobiliario, name = "mobiliario_list"),
    path("mobiliario", crearMobiliario, name = "mobiliarios_form"),
    path("mobiliario/<int:numero_serie>/eliminado", eliminar_item, name = "eliminar_item"),
    path("mobiliario/<int:numero_serie>/modificado", modificar_item, name = "modificar_item"),
    path("mobiliario/<int:numero_serie>/mobiliario_detalle", MobiliarioDetailView.as_view(), name = "mobiliario_detail"),

]
