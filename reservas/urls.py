from django.urls import path
from reservas.views import *

urlpatterns = [
    # Cancha
    path("canchas/", CanchaListView.as_view() , name = 'canchas_list'),
    path("cancha/nuevo/", CanchaCreateView.as_view() , name = 'cancha_create'),
    path("<str:code>/cancha_detalle", CanchaDetailView.as_view() , name = 'cancha_detail'),
    path("<str:code>/cancha_modificar/", CanchaUpdateView.as_view() , name = 'cancha_update'),
    path("<str:code>/cancha_eliminar/", CanchaDeleteView.as_view() , name = 'cancha_delete'),
    
    # Medico
    path("medicos/", MedicoListView.as_view() , name = 'medicos_list'),
    path("medico/nuevo/", MedicoCreateView.as_view() , name = 'medico_create'),
    path("<str:code>/medico_detalle", MedicoDetailView.as_view() , name = 'medico_detail'),
    path("<str:code>/medico_modificar/", MedicoUpdateView.as_view() , name = 'medico_update'),
    path("<str:code>/medico_eliminar/", MedicoDeleteView.as_view() , name = 'medico_delete')

]
