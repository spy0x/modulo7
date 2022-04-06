from django.db import models

# Create your models here.
class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)

class Comuna(models.Model):
    #se omite el id para que la ORM lo genere automaticamente
    name = models.CharField(max_length=50, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)

class UserType(models.Model):
    type = models.CharField(max_length=25, primary_key=True)
    can_admin = models.BooleanField(default=False) #Campo que potencialmente podría usarse para crear un Superusuario con seccion especial
    can_list_inmuebles = models.BooleanField(default=True) #Para que los arrendatarios puedan listar propiedades por comuna
    can_request_inmuebles = models.BooleanField(default=True) #Para que los arrendatarios puedan solicitar inmubles
    can_list_propiedades = models.BooleanField(default=False) #Para que los arrendadores puedan listar sus propiedades en su dashboard

class User(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    primer_nombre = models.CharField(max_length=50, null=False, blank=False)
    segundo_nombre = models.CharField(max_length=50, default='')
    primer_apellido = models.CharField(max_length=50, null=False, blank=False)
    segundo_apellido = models.CharField(max_length=50, default='')
    direccion = models.CharField(max_length=100, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    telefono = models.IntegerField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    user_type = models.ForeignKey(UserType, on_delete=models.PROTECT)

class Inmueble(models.Model):
    #se omite el id para que la ORM lo genere automaticamente    
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.TextField(max_length=255, null=False, blank=False)
    m2_construidos = models.IntegerField(null=False, blank=False)
    m2_totales = models.IntegerField(null=False, blank=False)
    n_estacionamientos = models.IntegerField(null=False, blank=False)
    n_habitaciones = models.IntegerField(null=False, blank=False)
    n_banos = models.IntegerField(null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    TIPO_CHOICES = [
        ('Casa', 'Casa'),
        ('Departamento', 'Departamento'),
        ('Parcela', 'Parcela'),
    ]
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES, default='Casa')
    precio_mensual = models.IntegerField(null=False, blank=False)
    arrendador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='arrendador')
    arrendatario = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='arrendatario', null=True, blank=True)

class SolicitudArriendo(models.Model):
    #se omite el id para que la ORM genere automaticamente
    user_request = models.ForeignKey(User, on_delete=models.CASCADE)
    inmueble_request = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
