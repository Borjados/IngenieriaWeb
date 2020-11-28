from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auto/<int:coches_id>/', views.autos, name='autos'),
    path('marca/', views.marca, name='marca'),
    path('categoria/', views.categoria, name='categoria'),
    path('vendedor/', views.vendedor, name='vendedor')
]