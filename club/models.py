from django.db import models

# Create your models here.
class Jugadores(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField(unique = True)
    años = models.DecimalField(max_digits=2, decimal_places= 0)
    fecha_nacimiento = models.DateField()
    dorsal = models.DecimalField(max_digits=2, decimal_places=0, unique=True)
    apodo = models.CharField(max_length=45, null = True)
    fecha_contratacion = models.DateField(null = True)
    #fecha_fin_contrato = models.DateField(null = True)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Dorsal: {self.años}"
    
    
class Patrocinadores(models.Model):
    nombre = models.CharField(max_length=100)
    numero_interno = models.IntegerField(unique = True)
    fecha_incorporacion = models.DateField(null = True)
    financiamiento = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha de incorporacion: {self.fecha_incorporacion}"
    

class Mobiliario(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    marca = models.CharField(max_length = 75)
    numero_serie = models.IntegerField(unique=True)
    
    def __str__(self):
        return f"Nombre {self.nombre} - Cantidad: {self.cantidad} - Marca: {self.marca}"
    