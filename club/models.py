from django.db import models

# Create your models here.
class Jugadores(models.Model):
    nombre = models.CharField(max_length=100, null = True)
    apellido = models.CharField(max_length=100, null = True)
    dni = models.IntegerField(null = True)
    años = models.DecimalField(max_digits=2, decimal_places= 0, null = True)
    fecha_nacimiento = models.DateField(null=True)
    dorsal = models.DecimalField(max_digits=2, decimal_places=0, unique=True, null = True)
    apodo = models.CharField(max_length=45, null = True)
    fecha_incorporacion = models.DateField(null = True)
    #fecha_fin_contrato agregar TODO
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Dorsal: {self.años}"
    
    
class Patrocinadores(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_fundacion = models.DateField(null = True)
    financiamiento = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha de fundacion: {self.fecha_fundacion}"
    

class Mobiliario (models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    marca = models.CharField(max_length = 75)
    
    def __str__(self):
        return f"Nombre {self.nombre} - Cantidad: {self.cantidad} - Marca: {self.marca}"
    