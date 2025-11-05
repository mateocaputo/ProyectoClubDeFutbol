from django.urls import path
from club.views import *

urlpatterns = [
    path("", index, name = "index"),
    path("about/", about_me, name = "about_me"),
    
    path("jugadores", crearJugador, name = "jugadores_form"),
    path("jugadores/busqueda", listar_jugadores, name = "jugadores_list"),
    path("jugadores/<int:dni>/eliminado", eliminar_jugador, name = "eliminar_jugador"),
    path("jugadores/<int:dni>/confirmar_eliminacion", eliminar_jugador_confirmacion, name = "eliminar_jugador_confirmacion"),
    
    path("jugadores/<int:dni>/modificado", modificar_jugador, name = "modificar_jugador"),
    path("jugadores/<int:dni>/confirmar_modificar", confirm_modif_jugador, name = "confirm_modif_jugador"),
    
    path("jugadores/<int:dni>/jugador_detalle", JugadorDetailView.as_view(), name = "jugador_detail"),


    path("patrocinadores/busqueda", listar_patrocinadores, name = "patrocinadores_list"),
    path("patrocinadores", crearPatrocinador, name = "patrocinadores_form"),
    path('patrocinadores/<int:numero_interno>/eliminado/', eliminar_patrocinador, name='eliminar_patrocinador'),
    path('patrocinadores/<int:numero_interno>/confirmar_eliminacion', eliminar_patrocinador_confirmacion, name='eliminar_patrocinador_confirmacion'),
    
    path("patrocinador/<int:numero_interno>/modificado", modificar_patrocinador, name = "modificar_patrocinador"),
    path("patrocinador/<int:numero_interno>/confirmar_modificar", confirm_modif_patrocinador, name = "confirm_modif_patrocinador"),
    
    path("patrocinador/<int:numero_interno>/patrocinador_detalle", PatrocinadorDetailView.as_view(), name = "patrocinador_detail"),
    
    
    
    path("mobiliario/busqueda", listar_mobiliario, name = "mobiliario_list"),
    path("mobiliario", crearMobiliario, name = "mobiliarios_form"),
    path('mobiliario/<int:numero_serie>/eliminado', eliminar_mobiliario, name='eliminar_mobiliario'),
    path('mobiliario/<int:numero_serie>/confirmar_eliminacion/',eliminar_mobiliario_confirmacion, name='eliminar_mobiliario_confirmacion'),
    
    
    path("mobiliario/<int:numero_serie>/modificado", modificar_item, name = "modificar_item"),
    path("mobiliario/<int:numero_serie>/confirmar_modificar", confirm_modif_item, name = "confirm_modif_item"),
    
    path("mobiliario/<int:numero_serie>/mobiliario_detalle", MobiliarioDetailView.as_view(), name = "mobiliario_detail"),

]
