from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import Perfil
from django import forms

class PerfilCreationForm(UserCreationForm):
    class Meta:
        model = Perfil
        fields = ["username", "email", "fecha_de_nacimiento", "direccion", "pais"]
        widgets = {
            "fecha_de_nacimiento" : forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
        }
class PerfilChangeForm(UserChangeForm):
    class Meta:
        model = Perfil
        fields = ['pais', 'imagen_perfil', 'fecha_de_nacimiento', 'direccion'] # ¡Importante! Define solo los campos que quieres modificar.
        # Asegura el estilo de Bootstrap para los campos
        widgets = {
            "fecha_de_nacimiento": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            "direccion": forms.TextInput(attrs={'class': 'form-control'}),
            "pais": forms.TextInput(attrs={'class': 'form-control'}),
            # El campo de archivo (FileField) usa 'form-control' por defecto o 'form-file' en versiones anteriores de Bootstrap
        }
        