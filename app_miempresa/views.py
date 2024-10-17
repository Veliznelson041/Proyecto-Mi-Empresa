import os
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

# Create your views here.
from .models import Cliente
from .forms import ClienteForm

def index(request):
    return render(request, 'app_miempresa/index.html')


def listado(request):
    clientes = Cliente.objects.all()
    return render(request, 'app_miempresa/listado.html', {'clientes':clientes})

def nuevo_cliente(request):
    if request.method == 'POST':
        formcliente = ClienteForm(request.POST, request.FILES)
        if formcliente.is_valid():
            formcliente.save()
            messages.success(request, 'Cliente creado exitosamente.')
            return redirect('index')
        else:
            messages.error(request, 'Atención: Verifique los datos Ingresados')
    else:
        formcliente = ClienteForm()
    return render(request, 'app_miempresa/nuevo_cliente.html', {'formcliente': formcliente})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    formcliente = ClienteForm(instance=cliente)
    if request.method == 'POST':
        formcliente = ClienteForm(request.POST, request.FILES, instance=cliente)
        if formcliente.is_valid():
            formcliente.save()
            messages.success(request, 'Cliente Editado exitoasamente.')
            return redirect('listado')
        else:
            messages.error(request, 'Atención: Verifique los Datos Ingresados')
    return render(request, 'app_empresa/editar_cliente.html', {'formcliente':formcliente})

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    #Guarda la ruta del archivo del campo ImageField antes de eliminar la instancia
    archivo = cliente.imagen.path
    #Elimina la instancia del modelo
    cliente.delete()
    #Verifica si el archivo existe y eliminarlo
    if os.path.exists(archivo):
        os.remove(archivo)
    return redirect('listado')