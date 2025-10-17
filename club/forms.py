from django import forms
from club.models import Jugadores

class JugadoresForms(forms.models):
    class Meta:
        model = Jugadores
        fields = ["nombre", "apellido", "dni","años", "fecha_nacimiento","dorsal", "apodo"]
        widgets = {
            "nombre" : forms.TextInput(attrs = {'class': 'form-control'}),
            "apellido" : forms.TextInput(attrs = {'class': 'form-control'}),
            "dni" : forms.NumberInput(attrs = {'class': 'form-control'}),
            "años" : forms.NumberInput(attrs = {'class': 'form-control'}),
            "fecha_nacimiento" : forms.DateInput(attrs = {'type': 'date', 'class': 'form-control'}),
            "dorsal" : forms.NumberInput(attrs = {'class': 'form-control'}),
            "apodo" : forms.TextInput(attrs = {'class': 'form-control'}),       
        }
    