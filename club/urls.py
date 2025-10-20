from django.urls import path
from club.views import index, crearJugador, crearPatrocinador, crearMobiliario

urlpatterns = [
    path("", index, name = "index"),
    path("jugadores", crearJugador, name = "jugadores_form"),
    path("patrocinadores", crearPatrocinador, name = "patrocinadores_form"),
    path("mobiliario", crearMobiliario, name = "mobiliarios_form"),
]
