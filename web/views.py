from django.shortcuts import render, redirect
from web.models import *
from web.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def RegisterView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_tipo?user=' + str(form.cleaned_data['username']))
    else:
        form = UserForm()

    context = {
        'form': form, 
    }
    return render(request, 'registration/register.html', context)

def Register_TipoView(request):
    username = request.GET['user']
    if request.method == 'POST':
        form = TipoForm(request.POST)
        if form.is_valid():
            form = TipoForm(request.POST)
            print(form)
            tipo = form.cleaned_data['tipo']
            rut = form.cleaned_data['rut']
            direccion = form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono']
            user = User.objects.filter(username=username)[0]
            tipo_user = UserType.objects.get(type=tipo)
            datos = UserProfile(user=user, user_type=tipo_user, rut=rut, direccion=direccion, telefono=telefono) #Faltan mas campos por rellenar los datos del formulario.
            datos.save()
            return HttpResponseRedirect('/login/')
    else:
        form = TipoForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/register_tipo.html', context)

@login_required
def DashboardView(request):
    return render(request, 'dashboard.html')

@login_required
def IndexView(request):
    return render(request, 'index.html')


# Create your views here.
