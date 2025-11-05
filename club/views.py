from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from club.forms import *
from club.models import *
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def about_me(request):
    return render(request, "club/about_me.html")

def index(request):
    return render(request, "club/index.html")

@login_required
def crearJugador(request):
    # GET - Pedir info
    # POST - Solicitud para crear
    if request.method == "POST":
        form = JugadoresForms(request.POST)
        if form.is_valid():
            jugador = form.save()
            messages.success(request, f"El jugador con dni {jugador.dni} a sido creado correctamente")
            return redirect("jugadores_list")
    else:
        form = JugadoresForms()
        
    
    return render(request, "club/jugadores.html", {'form':form})

@login_required
def crearPatrocinador(request):
    if request.method == "POST":
        form = PatrocinadoresForms(request.POST)
        if form.is_valid():
            patrocinador = form.save()
            messages.success(request, f"El patrocinador con numero de interno {patrocinador.numero_interno} a sido creado correctamente")
            return redirect("patrocinadores_list")
    else:
        form = PatrocinadoresForms()
    return render(request, "club/patrocinadores.html", {'form':form})

@login_required
def crearMobiliario(request):
    if request.method == "POST":
        form = MobiliarioForms(request.POST)
        if form.is_valid():
            mobiliario = form.save()
            messages.success(request, f"El mobiliario con numero de serie {mobiliario.numero_serie} a sido creado correctamente")
            return redirect("mobiliario_list")
    else:
        form = MobiliarioForms()
    return render(request, "club/mobiliarios.html", {'form':form})

@login_required
def listar_jugadores(request):
    query = request.GET.get('q', '')
    if len(query) > 0:
        jugadores = Jugadores.objects.filter(nombre__icontains = query).order_by("-apellido")
    else:
        jugadores = Jugadores.objects.all().order_by("-apellido")
    
    return render(request, "club/jugadores_list.html", {"jugadores": jugadores, "query":query})

@login_required
def listar_patrocinadores(request):
    query = request.GET.get('q', '')
    if len(query) > 0:
        patrocinadores = Patrocinadores.objects.filter(nombre__icontains = query).order_by("-numero_interno")
    else:
        patrocinadores = Patrocinadores.objects.all().order_by("-numero_interno")
    
    return render(request, "club/patrocinadores_list.html", {"patrocinadores": patrocinadores, "query":query})

@login_required
def listar_mobiliario(request):
    query = request.GET.get('q', '')
    if len(query) > 0:
        mobiliario = Mobiliario.objects.filter(nombre__icontains = query).order_by("-nombre")
    else:
        mobiliario = Mobiliario.objects.all().order_by("-nombre")
    
    return render(request, "club/mobiliario_list.html", {"mobiliario": mobiliario, "query":query})

@login_required
def eliminar_jugador_confirmacion(request, dni):
    jugador = get_object_or_404(Jugadores, dni=dni)
    contexto = {
        'object': jugador,
        'dni': dni
    }
    return render(request, 'club/jugador_delete.html', contexto)


# --- 2. VISTA DE ELIMINACIÓN (Ejecuta la acción) ---
@login_required
def eliminar_jugador(request, dni):
    if request.method == 'POST':
        jugador = get_object_or_404(Jugadores, dni=dni)
        
        # Ejecuta la eliminación
        jugador.delete()
        
        messages.success(request, f"El jugador con DNI Nro {dni} ha sido eliminado correctamente.")
        
        # Redirige a la lista después de la eliminación
        return redirect('jugadores_list')
    
    # Si alguien intenta acceder a esta URL directamente con GET, lo redirigimos a la confirmación
    return redirect('eliminar_jugador_confirmacion', dni=dni)




@login_required
def modificar_jugador(request, dni):
    jugador = get_object_or_404(Jugadores, dni = dni)
    if request.method == 'POST':
        form = JugadoresFormsEdit(request.POST, instance=jugador)
        if form.is_valid():
            jugador = form.save()
            messages.success(request, f"El jugador con nro de dni {jugador.dni} a sido modificado correctamente")
            return redirect("jugadores_list")
    else:
        form = JugadoresFormsEdit(instance = jugador) # Puedo cambiar el formulario para restringir datos
    return render(request, "club/jugadores.html", {'form':form, 'edicion':True})

@login_required
def confirm_modif_jugador(request, dni):
    jugador = get_object_or_404(Jugadores, dni = dni)
    contexto = {
        'object': jugador,
        'campo_identificador': dni # Valor necesario para la URL de eliminación
    }
    return render(request, 'club/jugador_updateConfirm.html', contexto)

@login_required
def eliminar_patrocinador_confirmacion(request, numero_interno):
    patrocinador = get_object_or_404(Patrocinadores, numero_interno=numero_interno)
    
    contexto = {
        'object': patrocinador,
        'nombre_objeto': patrocinador.nombre, # Campo identificador para el template
        'campo_identificador': numero_interno # Valor necesario para la URL de eliminación
    }
    return render(request, 'club/patrocinador_delete.html', contexto)

@login_required
def eliminar_patrocinador(request, numero_interno):
    if request.method == 'POST':
        patrocinador = get_object_or_404(Patrocinadores, numero_interno=numero_interno)
        patrocinador.delete()
        messages.success(request, f"El patrocinador '{patrocinador.nombre}' ha sido eliminado correctamente.")
        return redirect('patrocinadores_list')
    
    # Si es GET, lo enviamos a la confirmación
    return redirect('eliminar_patrocinador_confirmacion', numero_interno=numero_interno)
    
@login_required
def modificar_patrocinador(request, numero_interno):
    item = get_object_or_404(Patrocinadores, numero_interno = numero_interno)
    if request.method == 'POST':
        form = PatrocinadoresFormsEdit(request.POST, instance=item)
        if form.is_valid():
            patrocinador = form.save()
            messages.success(request, f"El patrocinador con numero de interno {patrocinador.numero_interno} a sido modificado correctamente")
            return redirect("patrocinadores_list")
    else:
        form = PatrocinadoresFormsEdit(instance = item) # Puedo cambiar el formulario para restringir datos
    return render(request, "club/patrocinadores.html", {'form':form, 'edicion':True})

@login_required
def confirm_modif_patrocinador(request, numero_interno):
    patrocinador = get_object_or_404(Patrocinadores, numero_interno = numero_interno)
    contexto = {
        'object': patrocinador
    }
    return render(request, 'club/patrocinador_updateConfirm.html', contexto)

@login_required
def eliminar_mobiliario_confirmacion(request, numero_serie):
    mobiliario = get_object_or_404(Mobiliario, numero_serie=numero_serie)
    
    contexto = {
        'object': mobiliario
    }
    return render(request, 'club/mobiliario_delete.html', contexto)

@login_required
def eliminar_mobiliario(request, numero_serie):
    if request.method == 'POST':
        mobiliario = get_object_or_404(Mobiliario, numero_serie=numero_serie)
        mobiliario.delete()
        messages.success(request, f"El mobiliario '{mobiliario.nombre}' ha sido eliminado correctamente.")
        return redirect('mobiliario_list')
    
    return redirect('eliminar_mobiliario_confirmacion', numero_serie=numero_serie)

@login_required  
def modificar_item(request, numero_serie):
    item = get_object_or_404(Mobiliario, numero_serie = numero_serie)
    if request.method == 'POST':
        form = MobiliarioFormsEdit(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            messages.success(request, f"El item con numero de serie {item.numero_serie} a sido modificado correctamente")
            return redirect("mobiliario_list")
    else:
        form = MobiliarioFormsEdit(instance = item) # Puedo cambiar el formulario para restringir datos
    return render(request, "club/mobiliarios.html", {'form':form, 'edicion':True})

@login_required
def confirm_modif_item(request, numero_serie):
    item = get_object_or_404(Mobiliario, numero_serie = numero_serie)
    contexto = {
        'object': item
    }
    return render(request, 'club/mobiliario_updateConfirm.html', contexto)

class JugadorDetailView(LoginRequiredMixin, DetailView):
    model = Jugadores
    template_name = "club/jugador_detail.html"
    context_object_name = "jugador"
    slug_field = 'dni'
    slug_url_kwarg = 'dni'
    
class PatrocinadorDetailView(LoginRequiredMixin, DetailView):
    model = Patrocinadores
    template_name = "club/patrocinador_detail.html"
    context_object_name = "patrocinador"
    slug_field = 'numero_interno'
    slug_url_kwarg = 'numero_interno'
    
class MobiliarioDetailView(LoginRequiredMixin, DetailView):
    model = Mobiliario
    template_name = "club/mobiliario_detail.html"
    context_object_name = "mobiliario"
    slug_field = 'numero_serie'
    slug_url_kwarg = 'numero_serie'




