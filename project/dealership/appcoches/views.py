from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Coches, Vendedor, Categoria, Marca

# Create your views here.

def index(request):
    ofertas = get_list_or_404(Coches.objects.order_by('-oferta'))
    context = { 'lista_coches': ofertas }
    return render(request, 'index.html', context)
    
def autos(request, coches_id):
    autos = get_object_or_404(Coches, pk=coches_id)
    context = { 'autos': autos }
    return render(request, 'coches.html', context)
    
def marca(request):
    marca = get_list_or_404(Marca.objects.order_by('nombre'))
    context = { 'lista_marcas': marca}
    return render(request, 'marca.html', context)
    
def categoria(request):
    categoria = get_list_or_404(Categoria.objects.order_by('nombre'))
    context = { 'lista_categorias': categoria}
    return render(request, 'categoria.html', context)
    
def vendedor(request):
    vendedor = get_list_or_404(Vendedor.objects.order_by('nombre'))
    context = { 'lista_vendedores': vendedor}
    return render(request, 'vendedor.html', context)

# Create your views here.
