from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=250)
    plataforma = models.CharField(max_length=100)
    comentario = models.CharField(max_length=1500)
    rating = models.IntegerField()