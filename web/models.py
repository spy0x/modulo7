from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)

class Comuna(models.Model):
    #se omite el id para que la ORM lo genere automaticamente
    name = models.CharField(max_length=50, null=False, blank=False)

class UserType(models.Model):
    type = models.CharField(max_length=25, primary_key=True)

class InmuebleType(models.Model):
    type = models.CharField(max_length=25, primary_key=True)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    rut = models.CharField(max_length=10, primary_key=True)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    telefono = models.IntegerField(null=False, blank=False)
    user_type = models.ForeignKey(UserType, on_delete=models.PROTECT)

class Inmueble(models.Model):
    #se omite el id para que la ORM lo genere automaticamente    
    nombre = models.CharField(max_length=255, null=False, blank=False, unique=True)
    descripcion = models.TextField(max_length=500, null=False, blank=False)
    m2_construidos = models.IntegerField(null=False, blank=False)
    m2_totales = models.IntegerField(null=False, blank=False)
    n_estacionamientos = models.IntegerField(null=False, blank=False)
    n_habitaciones = models.IntegerField(null=False, blank=False)
    n_banos = models.IntegerField(null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    tipo = models.ForeignKey(InmuebleType, on_delete=models.PROTECT)
    precio_mensual = models.IntegerField(null=False, blank=False)
    arrendador = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='arrendador')
    arrendatario = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, related_name='arrendatario', null=True, blank=True)

class SolicitudArriendo(models.Model):
    #se omite el id para que la ORM genere automaticamente
    user_request = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    inmueble_request = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
