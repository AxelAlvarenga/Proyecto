
from django.db import models
from django.db.models.base import ModelState

# Create your models here.


class Usuarios(models.Model):
    nombre_usuario = models.CharField(max_length = 50,primary_key=True, null=False)
    password_usuario = models.CharField(max_length = 50)
    nombre_completo_usuario = models.CharField(max_length = 200)

class producto(models.Model):
    codigo_productos=models.IntegerField(primary_key=True)
    nombre_productos= models.CharField(max_length = 50)
    preciocompra_productos= models.IntegerField()
    precioventa_productos= models.IntegerField()
    categoria_productos= models.CharField(max_length = 50)
    cantidad_productos=models.IntegerField()