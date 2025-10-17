from django.urls import path
from club.views import index, jugadores, patrocinadores, mobiliario

urlpatterns = [
    path("", index, name = "index"),
    path("jugadores", jugadores, name = "jugadores"),
    path("patrocinadores", patrocinadores, name = "patrocinadores"),
    path("mobiliario", mobiliario, name = "mobiliario"),
]
