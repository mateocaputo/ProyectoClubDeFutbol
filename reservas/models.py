from django.db import models
import uuid

def generar_code():
    return uuid.uuid4().hex


class Cancha(models.Model):
    # Nro de cancha
    nro_cancha = models.DecimalField(unique=True, decimal_places=0, max_digits=1)
    # Tipo de cancha F5, F7, F8, F9, F11
    tipo = models.CharField()
    # Descripcion de la misma
    descripcion = models.CharField(max_length=100)
    # Fecha de alta de la misma
    fecha_alta = models.DateTimeField(auto_now_add=True)
    # Codigo identificatorio
    code = models.CharField(
        max_length=32,
        unique=True,
        default= generar_code
    )
    
    def __str__(self):
        return f"{self.nro_cancha} - Nro: {self.tipo}"
    
class Medico(models.Model):
    nombre = models.CharField(max_length=75)
    apellido  = models.CharField(max_length=75)
    dni = models.DecimalField(unique=True, decimal_places=0, max_digits=8)
    nro_matricula = models.DecimalField(unique=True, decimal_places=0, max_digits=6)
    telefono = models.IntegerField()
    especialidad = models.CharField(max_length=100)
    code = models.CharField(
        max_length=32,
        unique=True,
        default= generar_code
    )
    
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - DNI: {self.dni}"
    
    
    
    
