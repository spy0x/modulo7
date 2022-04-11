from django.shortcuts import render, redirect
from web.models import *
from web.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def RegisterView(request):
    if request.method == "POST":
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

# Create your views here.
