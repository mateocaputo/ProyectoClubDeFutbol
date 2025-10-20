from django.shortcuts import render, redirect
from club.forms import *

# Create your views here.
def index(request):
    return render(request, "club/index.html")

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
            return redirect("jugadores_form")
    else:
        form = JugadoresForms()
    return render(request, "club/jugadores.html", {'form':form})

def crearPatrocinador(request):
    if request.method == "POST":
        form = PatrocinadoresForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("patrocinadores_form")
    else:
        form = PatrocinadoresForms()
    return render(request, "club/patrocinadores.html", {'form':form})

def crearMobiliario(request):
    if request.method == "POST":
        form = MobiliarioForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mobiliarios_form")
    else:
        form = MobiliarioForms()
    return render(request, "club/mobiliarios.html", {'form':form})