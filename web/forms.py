from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
    comuna = forms.CharField(label='Comuna', max_length=50)
    region = forms.IntegerField(label='Región')
    telefono = forms.CharField(label='Teléfono', max_length=9)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']