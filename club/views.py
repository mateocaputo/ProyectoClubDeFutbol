from django.shortcuts import render, redirect
from club.forms import *
from club.models import *

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
            return redirect("jugadores_list")
    else:
        form = JugadoresForms()
    return render(request, "club/jugadores.html", {'form':form})

def crearPatrocinador(request):
    if request.method == "POST":
        form = PatrocinadoresForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("patrocinadores_list")
    else:
        form = PatrocinadoresForms()
    return render(request, "club/patrocinadores.html", {'form':form})

def crearMobiliario(request):
    if request.method == "POST":
        form = MobiliarioForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mobiliario_list")
    else:
        form = MobiliarioForms()
    return render(request, "club/mobiliarios.html", {'form':form})

def listar_jugadores(request):
    query = request.GET.get('q', '')
    if len(query) > 0:
        jugadores = Jugadores.objects.filter(nombre__icontains = query).order_by("-apellido")
    else:
        jugadores = Jugadores.objects.all().order_by("-apellido")
    
    return render(request, "club/jugadores_list.html", {"jugadores": jugadores, "query":query})

def listar_patrocinadores(request):
    query = request.GET.get('q', '')
    if len(query) > 0:
        patrocinadores = Patrocinadores.objects.filter(nombre__icontains = query).order_by("-numero_interno")
    else:
        patrocinadores = Patrocinadores.objects.all().order_by("-numero_interno")
    
    return render(request, "club/patrocinadores_list.html", {"patrocinadores": patrocinadores, "query":query})

def listar_mobiliario(request):
    query = request.GET.get('q', '')
    if len(query) > 0:
        mobiliario = Mobiliario.objects.filter(nombre__icontains = query).order_by("-nombre")
    else:
        mobiliario = Mobiliario.objects.all().order_by("-nombre")
    
    return render(request, "club/mobiliario_list.html", {"mobiliario": mobiliario, "query":query})