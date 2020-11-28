from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auto/<int:coches_id>/', views.autos, name='autos'),
    path('marca/', views.marca, name='marca'),
    path('marca/<int:marca_id>/', views.listamarca, name='listamarca'),
    path('categoria/', views.categoria, name='categoria'),
    path('categoria/<int:categoria_id>/', views.listacategoria, name='listacategoria'),
    path('vendedor/', views.vendedor, name='vendedor'),
     path('vendedor/<int:vendedor_id>/', views.listavendedor, name='listavendedor'),
    path('signIn/', views.signIn, name = 'signIn'),
    path('signIn/crearCuenta/', views.crearCuenta, name = 'crearCuenta'),
    path('comprar/', views.comprar, name='comprar')

]