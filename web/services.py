from web.models import Region, Comuna, UserType, User, Inmueble, SolicitudArriendo

def crear_inmueble(
    nombre: str, 
    descripcion: str, 
    m2_construidos: int, 
    m2_totales: int, 
    n_estacionamientos: int,
    n_habitaciones: int,
    n_banos: int,
    direccion: str,
    region_id: int,
    comuna_name: str,
    tipo: str,
    precio_mensual: int,
    arrendador_rut: str,
    arrendatario_rut: str = None): #Este parametro es adicional por si se quiere agregar un arrendatario al momento de la creacion misma del inmueble.

    region = Region.objects.get(pk=region_id)
    comuna = Comuna.objects.get(name=comuna_name, region=region)
    arrendador = User.objects.get(pk=arrendador_rut)
    arrendatario = User.objects.get(pk=arrendatario_rut) if arrendatario_rut != None else None
    
    inmueble = Inmueble(
        nombre=nombre, 
        descripcion=descripcion, 
        m2_construidos=m2_construidos,
        m2_totales=m2_totales,
        n_estacionamientos=n_estacionamientos,
        n_habitaciones=n_habitaciones,
        n_banos=n_banos,
        direccion=direccion,
        region=region,
        comuna=comuna,
        tipo=tipo,
        precio_mensual=precio_mensual,
        arrendador=arrendador,
        arrendatario=arrendatario)
    inmueble.save()

#Lista todos los inmuebles del arrendador. La funcion recibe el rut del arrendador.
def listar_inmuebles(arrendador_id: str):
    arrendador = User.objects.get(pk=arrendador_id)
    lista_propiedades = Inmueble.objects.filter(arrendador=arrendador)
    for index, propiedad in lista_propiedades:
        print(f"\n[{index+1}] {propiedad.name}\n{propiedad.descripcion}\nTipo: {propiedad.tipo}\nPrecio mensual: {propiedad.precio_mensual}\nArrendatario: {propiedad.arrendatario}")

#Lista todos los inmuebles de todos los arrendadores. Para que los clientes puedan ver todos los inmuebles.
def listar_inmuebles_all():
    lista_propiedades = Inmueble.objects.all()
    for index, propiedad in lista_propiedades:
        print(f"\n[{index+1}] {propiedad.name}\n{propiedad.descripcion}\nTipo: {propiedad.tipo}\nPrecio mensual: {propiedad.precio_mensual}\nArrendador: {propiedad.arrendador}")

#Elimina la propiedad indicada por su nombre (campo UNIQUE en la DB), y pide que se le envíe por seguridad también que coincida con el rut del arrendador correcto
def eliminar_inmueble(nombre_inmueble: str, arrendador_rut: str):
    arrendador = User.objects.get(pk=arrendador_rut)
    inmueble = Inmueble.objects.get(arrendador=arrendador, nombre=nombre_inmueble)
    inmueble.delete()