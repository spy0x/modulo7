from random import choices
from django.db import models

# Create your models here.
class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)

class Comuna(models.Model):
    #se omite el id para que la ORM lo genere automaticamente
    name = models.CharField(max_length=50, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

class UserType(models.Model):
    type = models.CharField(max_length=25, primary_key=True)
    canAdmin = models.BooleanField(default=False)

class User(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    primer_nombre = models.CharField(max_length=50, null=False, blank=False)
    segundo_nombre = models.CharField(max_length=50, default='')
    primer_apellido = models.CharField(max_length=50, null=False, blank=False)
    segundo_apellido = models.CharField(max_length=50, default='')
    direccion = models.CharField(max_length=100, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=False, blank=False)
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=False, blank=False)
    telefono = models.IntegerField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    user_type = models.ForeignKey(UserType, on_delete=models.SET_NULL, null=False, blank=False)

class Inmueble(models.Model):
    #se omite el id para que la ORM lo genere automaticamente    
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    m2_construidos = models.IntegerField(null=False, blank=False)
    m2_totales = models.IntegerField(null=False, blank=False)
    n_estacionamientos = models.IntegerField(null=False, blank=False)
    n_habitaciones = models.IntegerField(null=False, blank=False)
    n_banos = models.IntegerField(null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=False, blank=False)
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=False, blank=False)
    TIPO_CHOICES = [
        ('C', 'Casa'),
        ('D', 'Departamento'),
        ('P', 'Parcela'),
    ]
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, default='C')
    precio_mensual = models.IntegerField(null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
