from django.shortcuts import render, redirect
from club.forms import *

# Create your views here.
def index(request):
    return render(request, "club/index.html")

def jugadores(request):
    return render(request, "club/jugadores.html")

def patrocinadores(request):
    return render(request, "club/patrocinadores.html")

def mobiliario(request):
    return render(request, "club/mobiliarios.html")

def crearJugador(request):
    # GET - Pedir info
    # POST - Solicitud para crear
    if request.method == "POST":
        form = JugadoresForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("jugadores")
    else:
        form = JugadoresForms()
    return request(request, "club/jugadores.html", {'form':form})