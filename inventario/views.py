from django.http import HttpResponse
from django.shortcuts import render
from .models import Categoria


def index(request):
    return HttpResponse("Hello World")

def contact(request, name):
    return HttpResponse(f"Hello {name}")

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, "categorias.html", {
        "categorias": categorias
    })
    
#############
def categoria_list(request):
  
    filtro_nombre = request.GET.get('nombre')
    if filtro_nombre:
        categorias = Categoria.objects.filter(nombre__icontains=filtro_nombre)
    else:
        categorias = Categoria.objects.all()  
    
    return render(request, 'inventario/categoria_list.html', {'categorias': categorias})