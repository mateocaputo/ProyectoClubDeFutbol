from django import forms
from club.models import Jugadores, Patrocinadores, Mobiliario

class JugadoresForms(forms.ModelForm):
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
        
class PatrocinadoresForms(forms.ModelForm):
    class Meta:
        model = Patrocinadores
        fields = ["nombre", "numero_interno", "fecha_incorporacion", "financiamiento"]
        widgets = {
            "nombre":forms.TextInput(attrs = {'class': 'form-control'}),
            "numero_interno": forms.NumberInput(attrs = {'class': 'form-control'}),
            "fecha_incorporacion":forms.DateInput(attrs = {'type':'date', 'class': 'form-control'}),
            "financiamiento":forms.NumberInput(attrs = {'class': 'form-control'})
        }
        
class MobiliarioForms(forms.ModelForm):
    class Meta:
        model = Mobiliario
        fields = ["nombre", "cantidad", "marca"]
        widgets = {
            "nombre":forms.TextInput(attrs = {'class': 'form-control'}),
            "cantidad":forms.NumberInput(attrs = {'class': 'form-control'}),
            "marca":forms.TextInput(attrs = {'class': 'form-control'})
        }