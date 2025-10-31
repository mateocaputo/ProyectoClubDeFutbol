from django import forms
from reservas.models import *

class CanchaForm(forms.ModelForm):
    class Meta:
        model = Cancha
        fields = ["nro_cancha", "tipo", "descripcion"]
        widgets = {
            "nro_cancha" : forms.NumberInput(attrs={'class': 'form-control'}),
            "tipo" : forms.TextInput(attrs={'class': 'form-control'}),
            "descripcion" : forms.TextInput(attrs={'class': 'form-control'})
        }

class CanchaFormEdit(forms.ModelForm):
    class Meta:
        model = Cancha
        fields = ["descripcion"]
        widgets = {
            "descripcion" : forms.TextInput(attrs={'class': 'form-control'})
        }
        
# -------------------------- MEDICO --------------------------

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ["nombre", "apellido", "dni", "nro_matricula", "telefono", "especialidad"]
        widgets = {
            "nombre" : forms.TextInput(attrs={'class': 'form-control'}),
            "apellido" : forms.TextInput(attrs={'class': 'form-control'}),
            "dni" : forms.NumberInput(attrs={'class': 'form-control'}),
            "nro_matricula" : forms.NumberInput(attrs={'class': 'form-control'}),
            "telefono" : forms.NumberInput(attrs={'class': 'form-control'}),
            "especialidad" : forms.TextInput(attrs={'class': 'form-control'}),
        }

class MedicoFormEdit(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ["telefono", "especialidad"]
        widgets = {
            "telefono" : forms.NumberInput(attrs={'class': 'form-control'}),
            "especialidad" : forms.TextInput(attrs={'class': 'form-control'})
        }
        
        