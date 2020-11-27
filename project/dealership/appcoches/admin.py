from django.contrib import admin
from .models import Coches, Vendedor, Marca, Categoria

admin.site.register(Coches)
admin.site.register(Vendedor)
admin.site.register(Marca)
admin.site.register(Categoria)

# Register your models here.
