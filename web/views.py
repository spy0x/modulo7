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
            comuna = form.cleaned_data['comuna']
            region = form.cleaned_data['region']
            telefono = form.cleaned_data['telefono']
            user = User.objects.filter(username=username)[0]
            tipo_user = UserType.objects.get(type=tipo)
            region_user = Region.objects.get(id=region)
            comuna_user = Comuna.objects.filter(name=comuna)[0]
            datos = UserProfile(user=user, user_type=tipo_user, rut=rut, direccion=direccion, telefono=telefono, region=region_user, comuna=comuna_user) #Faltan mas campos por rellenar los datos del formulario.
            datos.save()
            return HttpResponseRedirect('/')
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

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'u_form': u_form,
    }
    return render(request, 'registration/update_profile.html', context)

@login_required
def New_Inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            tipo_id = form.cleaned_data['tipo_inmueble']
            comuna_id = form.cleaned_data['comuna']
            region_id = form.cleaned_data['region']
            direccion = form.cleaned_data['direccion']
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            m2_construidos = form.cleaned_data['m2_construidos']
            m2_totales = form.cleaned_data['m2_totales']
            n_habitaciones = form.cleaned_data['n_habitaciones']
            n_banos = form.cleaned_data['n_banos']
            n_estacionamientos = form.cleaned_data['n_estacionamientos']
            precio_mensual = form.cleaned_data['precio_mensual']

            tipo = InmuebleType.objects.get(type=tipo_id)
            comuna = Comuna.objects.get(id=comuna_id)
            region = Region.objects.get(id=region_id)
            user = request.user
            arrendador = UserProfile.objects.get(user_id=user.id)

            inmueble = Inmueble(
                nombre=nombre, 
                descripcion=descripcion, 
                m2_construidos=m2_construidos, 
                m2_totales=m2_totales,
                n_estacionamientos=n_estacionamientos,
                n_habitaciones=n_habitaciones,
                n_banos=n_banos,
                direccion=direccion,
                precio_mensual=precio_mensual,
                tipo=tipo,
                region=region,
                comuna=comuna,
                arrendador=arrendador,
                )
            inmueble.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        form = InmuebleForm()
        
    context = {
        'form': form,
    }
    return render(request, 'new_inmueble.html', context)





# Create your views here.
