from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('auto/<int:coches_id>/', views.autos, name='autos')
]