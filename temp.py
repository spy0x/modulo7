import os
import time
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "modulo7.settings")
django.setup()
from web.models import Inmueble, Region, Comuna

#Lista todos los inmuebles ordenados por Comuna mostrando su Nombre y Descripcion.
def list_inmuebles_comuna():
    lista_inmuebles = Inmueble.objects.all().order_by('comuna_id')
    file = open("inmuebles_comuna.txt", "w")
    for inmueble in lista_inmuebles:
        file.write(f"{inmueble.comuna.name} --- Nombre: {inmueble.nombre} ---------- Descripción: {inmueble.descripcion}")
        file.write("\n")
    file.close()

#Lista todos los inmuebles ordenados por Region mostrando su Nombre y Descripcion.
def list_inmuebles_region():
    lista_inmuebles = Inmueble.objects.all().order_by('region_id')
    file = open("inmuebles_region.txt", "w")
    for inmueble in lista_inmuebles:
        file.write(f"{inmueble.region.name} --- Nombre: {inmueble.nombre} ---------- Descripción: {inmueble.descripcion}")
        file.write("\n")
    file.close()

#Lista todos los inmuebles de la comuna indicada. Muestra nombres y descripcion.
def search_inmuebles_comuna(comuna_id):
    comuna = Comuna.objects.get(id=comuna_id)
    lista_inmuebles = Inmueble.objects.filter(comuna=comuna)
    file = open("search_inmuebles_comuna.txt", "w")
    if len(lista_inmuebles) > 0:
        for inmueble in lista_inmuebles:
            file.write(f"{inmueble.region.name} --- Nombre: {inmueble.nombre} ---------- Descripción: {inmueble.descripcion}")
            file.write("\n")
    else:
        file.write(f"No hubo resultados.")
    file.close()

#Lista todos los inmuebles de la region indicada. Muestra nombres y descripcion.
def search_inmuebles_region(region_id):
    region = Region.objects.get(id=region_id)
    lista_inmuebles = Inmueble.objects.filter(region=region)
    file = open("search_inmuebles_region.txt", "w")
    if len(lista_inmuebles) > 0:
        for inmueble in lista_inmuebles:
            file.write(f"{inmueble.region.name} --- Nombre: {inmueble.nombre} ---------- Descripción: {inmueble.descripcion}")
            file.write("\n")
    else:
        file.write(f"No hubo resultados.")
    file.close()
