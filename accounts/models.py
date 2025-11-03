from django.db import models
from django.contrib.auth.models import AbstractUser


def imagen_perfil_upload_to(instance, filename):
    return f"imagenes_perfil/{instance.username}/{filename}"
# Se llama perfil porque asi lo defini en settings.py
class Perfil(AbstractUser):
    class Paises(models.TextChoices):
        # CONSTANTE       = VALOR_DB,   ETIQUETA_LEGIBLE
        ARGENTINA   = 'AR',       'Argentina'
        BRASIL      = 'BR',       'Brasil'
        CHILE       = 'CL',       'Chile'
        COLOMBIA    = 'CO',       'Colombia'
        ESPAÑA      = 'ES',       'España'
        OTRO        = 'OT',       'Otro'
        
    imagen_perfil = models.ImageField(
        upload_to = imagen_perfil_upload_to,
        default = "default/perfil/default.jpg",
        blank = True,
        null = True,
        verbose_name="Avatar"
    )
    pais = models.CharField(
        max_length=2,                   # Longitud máxima para VALOR_DB ('AR', 'BR', etc.)
        choices=Paises.choices,         # Lista de opciones que Django usará
        default=Paises.ARGENTINA,       # Establece un valor por defecto
        verbose_name="País de Origen"
    )
    fecha_de_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        
    def __str__(self):
        return f"{self.last_name} {self.first_name}, {self.username}"