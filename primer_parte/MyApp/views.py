from django.shortcuts import render  # type: ignore
from django.http import HttpRequest  # type: ignore
from .models import PlatosTipicosDeEcuador
from decimal import Decimal, InvalidOperation

# Create your views here.


def listPlatosTipicos(request: HttpRequest):
    context = {
        'platos':    PlatosTipicosDeEcuador.objects.all()
    }
    return render(request, 'listPlatosTipicos.html', context)


def addPlatoTipicoPost(request: HttpRequest):
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    ingredientes = request.POST['ingredientes']
    region = request.POST['region']
    precio = request.POST['precio']
    if precio.find('.') == -1:
        precio = precio + '.00'
    plato = PlatosTipicosDeEcuador(
        nombre=nombre, descripcion=descripcion, precio=Decimal(precio), region=region, ingredientes=ingredientes)
    plato.save()
    return render(request, 'addPlatoTipico.html', {'mensaje': 'Plato guardado'})


def addPlatoTipico(request: HttpRequest):
    if request.method == 'POST':
        return addPlatoTipicoPost(request)

    if request.method == 'GET':
        return render(request, 'addPlatoTipico.html')


def deletePlatoTipico(request: HttpRequest, id: int):
    plato = PlatosTipicosDeEcuador.objects.get(id=id)
    plato.delete()
    return render(request, 'listPlatosTipicos.html', {'platos': PlatosTipicosDeEcuador.objects.all(), 'mensaje': 'Plato eliminado'})


def editPlatoTipico(request: HttpRequest, id: int):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        ingredientes = request.POST['ingredientes']
        region = request.POST['region']
        precio = request.POST['precio']
        if precio.find('.') == -1:
            precio = precio + '.00'
        plato = PlatosTipicosDeEcuador.objects.get(id=id)
        plato.nombre = nombre
        plato.descripcion = descripcion
        plato.ingredientes = ingredientes
        plato.region = region
        plato.precio = Decimal(precio)
        plato.save()
        return render(request, 'listPlatosTipicos.html', {'platos': PlatosTipicosDeEcuador.objects.all(), 'mensaje': 'Plato actualizado'})

    if request.method == 'GET':
        plato = PlatosTipicosDeEcuador.objects.get(id=id)
        plato = PlatosTipicosDeEcuador.objects.get(id=id)
        context = {'plato': plato, 'id': id}
        return render(request, 'editPlatoTipico.html', context)
