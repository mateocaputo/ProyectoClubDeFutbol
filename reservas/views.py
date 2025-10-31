from django.shortcuts import render
from reservas.forms import * 
from reservas.models import *
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

class CanchaListView(ListView):
    model = Cancha
    template_name = "reservas/canchas_list.html"
    context_object_name = 'canchas'
    
    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return Cancha.objects.filter(tipo__icontains=query).order_by("-nro_cancha")
        return Cancha.objects.all()
    
class CanchaCreateView(CreateView):
    model = Cancha
    form_class = CanchaForm
    template_name = "reservas/cancha_form.html"
    success_url = reverse_lazy('canchas_list')
    
class CanchaUpdateView(UpdateView):
    model = Cancha
    form_class = CanchaFormEdit
    template_name = "reservas/cancha_form.html"
    success_url = reverse_lazy('canchas_list')
    slug_field = 'code'
    slug_url_kwarg = 'code'
    
class CanchaDeleteView(DeleteView):
    model = Cancha
    template_name = "reservas/cancha_delete.html"
    success_url = reverse_lazy('canchas_list')
    slug_field = 'code'
    slug_url_kwarg = 'code'

class CanchaDetailView(DetailView):
    model = Cancha
    template_name = "reservas/cancha_detail.html"
    context_object_name = "cancha"
    slug_field = 'code'
    slug_url_kwarg = 'code'

# ----------------------- MEDICOS -----------------------

class MedicoListView(ListView):
    model = Medico
    template_name = "reservas/medicos_list.html"
    context_object_name = 'medicos'
    
    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return Medico.objects.filter(apellido__icontains=query).order_by("-nro_matricula")
        return Medico.objects.all()
    
class MedicoCreateView(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = "reservas/medico_form.html"
    success_url = reverse_lazy('medicos_list')
    
class MedicoUpdateView(UpdateView):
    model = Medico
    form_class = MedicoFormEdit
    template_name = "reservas/medico_form.html"
    success_url = reverse_lazy('medicos_list')
    slug_field = 'code'
    slug_url_kwarg = 'code'
    
class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = "reservas/medico_delete.html"
    success_url = reverse_lazy('medicos_list')
    slug_field = 'code'
    slug_url_kwarg = 'code'

class MedicoDetailView(DetailView):
    model = Medico
    template_name = "reservas/medico_detail.html"
    context_object_name = "medico"
    slug_field = 'code'
    slug_url_kwarg = 'code'
    
    