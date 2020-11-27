from django.db import models

class Categoria (models.Model):
    nombre = models.CharField(max_length=75)
    url_categoria = models.CharField(max_length=2000)
    
class Vendedor (models.Model):
    nombre = models.CharField(max_length=75, null=True)
    apellido = models.CharField(max_length=75, null=True)
    email = models.CharField(max_length=200, null=True)
    telefono = models.IntegerField(default=0, null=True)
    rating = models.IntegerField(default=0, null=True)
    url_vendedor = models.CharField(max_length=2000, null=True)
    
class Marca(models.Model):
    nombre = models.CharField(max_length=75)
    url_marca = models.CharField(max_length=2000)

class Coches(models.Model):
    modelo = models.CharField(max_length=250)
    caballos = models.IntegerField(default=0)
    puertas = models.IntegerField(default=0)
    color = models.CharField(max_length=50)
    kilometros = models.IntegerField(default=0)
    año = models.IntegerField(default=0)
    matricula = models.CharField(max_length=50)
    oferta = models.BooleanField(default=False)
    precio = models.IntegerField(default=0)
    precio_oferta = models.IntegerField(default=0)
    #porcentaje = Coches.objects.all().annotate(100 - 100*(F('precio_oferta') / F('precio')))
    url_coche = models.CharField(max_length=2000)
    categoria = models.ManyToManyField(Categoria)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
# Create your models here.
