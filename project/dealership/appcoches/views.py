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
    return render(request, 'autos.html', context)

# Create your views here.
