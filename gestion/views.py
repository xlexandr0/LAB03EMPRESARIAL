from django.shortcuts import render, get_object_or_404, redirect
from .models import Propietario, Vehiculo, Registro
from .forms import PropietarioForm, VehiculoForm, RegistroForm

# Listar todos los propietarios
def listar_propietarios(request):
    propietarios = Propietario.objects.all()
    return render(request, 'gestion/listar_propietarios.html', {'propietarios': propietarios})

# Detalle de un propietario
def detalle_propietario(request, id):
    propietario = get_object_or_404(Propietario, id=id)
    return render(request, 'gestion/detalle_propietario.html', {'propietario': propietario})

# Editar un propietario
def editar_propietario(request, id):
    propietario = get_object_or_404(Propietario, id=id)
    if request.method == 'POST':
        form = PropietarioForm(request.POST, instance=propietario)
        if form.is_valid():
            form.save()
            return redirect('listar_propietarios')
    else:
        form = PropietarioForm(instance=propietario)
    return render(request, 'gestion/editar_propietario.html', {'form': form, 'propietario': propietario})


# Eliminar un propietario
def eliminar_propietario(request, id):
    propietario = get_object_or_404(Propietario, id=id)
    if request.method == 'POST':
        propietario.delete()
        return redirect('listar_propietarios')
    return render(request, 'gestion/eliminar_propietario.html', {'propietario': propietario})

# Registrar un nuevo propietario
def registrar_propietario(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_propietarios')
    else:
        form = PropietarioForm()
    return render(request, 'gestion/registrar_propietario.html', {'form': form})

# Página de inicio
def home(request):
    return render(request, 'gestion/home.html')

# Registrar un nuevo vehículo
def registrar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'gestion/registrar_vehiculo.html', {'form': form})

# Listar todos los vehículos
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'gestion/listar_vehiculos.html', {'vehiculos': vehiculos})

# Editar un vehículo
def editar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('listar_vehiculos')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'gestion/editar_vehiculo.html', {'form': form})

# Eliminar un vehículo
def eliminar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('listar_vehiculos')
    return render(request, 'gestion/eliminar_vehiculo.html', {'vehiculo': vehiculo})

# Detalle de un vehículo
def detalle_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    return render(request, 'gestion/detalle_vehiculo.html', {'vehiculo': vehiculo})

# Registrar un nuevo registro de entrada/salida
def registrar_registro(request):
    if request.method == 'POST':
        # Crear un formulario con los datos POST
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Guardar el nuevo registro en la base de datos
            form.save()
            # Redirigir a una página de éxito o a la lista de registros
            return redirect('listar_registros')
        else:
            # En caso de error en el formulario, mostrar el formulario con errores
            return render(request, 'gestion/registrar_registro.html', {'form': form, 'vehiculos': Vehiculo.objects.all()})
    else:
        # Mostrar el formulario vacío
        form = RegistroForm()
        return render(request, 'gestion/registrar_registro.html', {'form': form, 'vehiculos': Vehiculo.objects.all()})

# Listar todos los registros
def listar_registros(request):
    registros = Registro.objects.all()
    return render(request, 'gestion/listar_registros.html', {'registros': registros})

def detalle_registro(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    return render(request, 'gestion/detalle_registro.html', {'registro': registro})

def editar_registro(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    if request.method == 'POST':
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('listar_registros')
    else:
        form = RegistroForm(instance=registro)
    return render(request, 'gestion/editar_registro.html', {'form': form})

def eliminar_registro(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    if request.method == 'POST':
        registro.delete()
        return redirect('listar_registros')
    return render(request, 'gestion/eliminar_registro.html', {'registro': registro})