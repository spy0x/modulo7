import os
import time
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "modulo7.settings")
django.setup()
from web.models import Inmueble, Region, Comuna

def list_inmuebles_region():
    lista_inmuebles = Inmueble.objects.all().order_by('region_id')
    file = open("inmuebles_region.txt", "w")
    for inmueble in lista_inmuebles:
        file.write(f"{inmueble.region.name} --- Nombre: {inmueble.nombre} ---------- Descripción: {inmueble.descripcion}")
        file.write("\n")
    file.close()

def list_inmuebles_comuna():
    lista_inmuebles = Inmueble.objects.all().order_by('comuna_id')
    file = open("inmuebles_comuna.txt", "w")
    for inmueble in lista_inmuebles:
        file.write(f"{inmueble.comuna.name} --- Nombre: {inmueble.nombre} ---------- Descripción: {inmueble.descripcion}")
        file.write("\n")
    file.close()