from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comuna, Region, Inmueble

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class TipoForm(forms.Form):
    tipos = (('Arrendatario', 'Arrendatario'), ('Arrendador', 'Arrendador'),)
    tipo = forms.ChoiceField(choices=tipos, label='Tipo de Usuario')
    rut = forms.CharField(label='RUT', max_length=10)
    direccion = forms.CharField(label='Dirección', max_length=100)
    comunas = [(comuna.id, comuna.name) for comuna in Comuna.objects.order_by('name')]
    regiones = [(region.id, region.name) for region in Region.objects.order_by('id')]
    comuna = forms.ChoiceField(choices=comunas)
    region = forms.ChoiceField(choices=regiones)
    telefono = forms.CharField(label='Teléfono', max_length=9)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class InmuebleForm(forms.Form):
    tipos = (("Casa", "Casa"), ("Parcela", "Parcela"), ("Departamento", "Departamento"), ("Otro", "Otro"))
    tipo_inmueble = forms.ChoiceField(choices=tipos)
    comunas = [(comuna.id, comuna.name) for comuna in Comuna.objects.order_by('name')]
    regiones = [(region.id, region.name) for region in Region.objects.order_by('id')]
    comuna = forms.ChoiceField(choices=comunas)
    region = forms.ChoiceField(choices=regiones)
    direccion = forms.CharField(label="Dirección", max_length=100)
    nombre = forms.CharField(label="Nombre del inmueble", max_length=255)
    descripcion = forms.CharField(label="Descripcion", max_length=500)
    m2_construidos = forms.IntegerField(label="M2 Construidos")
    m2_totales = forms.IntegerField(label="M2 Terreno Total")
    n_habitaciones = forms.IntegerField(label="N° Habitaciones")
    n_banos = forms.IntegerField(label="N°Baños")
    n_estacionamientos = forms.IntegerField(label="N° Estacionamientos")
    precio_mensual = forms.IntegerField(label="Precio Mensual")

class InmueblesUpdateForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['nombre', 'descripcion', 'precio_mensual']