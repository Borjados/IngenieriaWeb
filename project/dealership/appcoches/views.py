from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Coches, Vendedor, Categoria, Marca

# Create your views here.

def index(request):
    ofertas = get_list_or_404(Coches.objects.order_by('precio_oferta'))
    ofertas_i =[]
    for oferta in ofertas:
        if(oferta.oferta == True):
            ofertas_i.append(oferta)
    context = { 'lista_coches': ofertas_i }
    return render(request, 'index.html', context)
    
def autos(request, coches_id):
    autos = get_object_or_404(Coches, pk=coches_id)
    categoria = autos.categoria.all()
    context = { 'autos': autos, 'categoria' : categoria }
    return render(request, 'coches.html', context)
    
def marca(request):
    marca = get_list_or_404(Marca.objects.order_by('nombre'))
    context = { 'lista_marcas': marca}
    return render(request, 'marca.html', context)

def listamarca(request, marca_id):
    x=get_object_or_404(Marca, pk=marca_id)
    marca = x.nombre
    coches = get_list_or_404(Coches.objects.order_by('modelo'))
    cochesmarca = []
    for coche in coches:
        if(coche.marca == x):
            cochesmarca.append(coche)
    context = { 'lista_cochesmarca': cochesmarca, 'marca' :  marca}
    return render(request, 'listamarca.html', context)
    
def categoria(request):
    categoria = get_list_or_404(Categoria.objects.order_by('nombre'))
    context = { 'lista_categorias': categoria}
    return render(request, 'categoria.html', context)
    
def listacategoria(request, categoria_id):
    x=get_object_or_404(Categoria, pk=categoria_id)
    c=x.nombre
    coches = get_list_or_404(Coches.objects.order_by('modelo'))
    cochescategoria = []
    for coche in coches:
        categorias = coche.categoria.all()
        for categoria in categorias:
            if(categoria == x):
                cochescategoria.append(coche)
    context = { 'lista_cochescategoria': cochescategoria, 'categoria' : c }
    return render(request, 'listacategoria.html', context)
    
def vendedor(request):
    vendedor = get_list_or_404(Vendedor.objects.order_by('nombre'))
    context = { 'lista_vendedores': vendedor}
    return render(request, 'vendedor.html', context)

def listavendedor(request, vendedor_id):
    x=get_object_or_404(Vendedor, pk=vendedor_id)
    vendedor = x.nombre
    coches = get_list_or_404(Coches.objects.order_by('modelo'))
    cochesvendedor = []
    for coche in coches:
        if(coche.vendedor == x):
            cochesvendedor.append(coche)
    context = { 'lista_cochesvendedor': cochesvendedor, 'vendedor' :  vendedor}
    return render(request, 'listavendedor.html', context)   

def signIn(request):
    return render(request, 'signIn.html')

def crearCuenta(request):
    return render(request, 'crearCuenta.html')

def comprar(request):
    return render(request, 'comprar.html')

# Create your views here.
