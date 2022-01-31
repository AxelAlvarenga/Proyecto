
from django.db import models
from django.db.models.base import ModelState

# Create your models here.


class Usuarios(models.Model):
    cod_usuario=models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length = 50)
    password_usuario = models.CharField(max_length = 50)
    nombre_completo_usuario = models.CharField(max_length = 200)

class cliente(models.Model):
    codigo_cliente=models.IntegerField(primary_key=True)
    nombre_cliente= models.CharField(max_length = 50)
    telefono_cliente= models.IntegerField()
    direccion_cliente=models.CharField(max_length=50)

class categoria(models.Model):
    codigo_categoria=models.AutoField(primary_key=True)
    nombre_categoria=models.CharField(max_length = 50)   

class proveedor(models.Model):
    codigo_proveedor=models.AutoField(primary_key=True)
    nombre_proveedor= models.CharField(max_length = 50)
    ruc_proveedor= models.CharField(max_length = 50)
    Telefono_proveedor= models.IntegerField()
    direccion_proveedor=models.CharField(max_length= 50)

class producto(models.Model):
    codigo_productos=models.IntegerField(primary_key=True)
    nombre_productos= models.CharField(max_length = 50)
    preciocompra_productos= models.IntegerField()
    precioventa_productos= models.IntegerField()
    categoria_productos= models.IntegerField()
    cantidad_productos=models.IntegerField()
    nombre_proveedor = models.ForeignKey(proveedor ,on_delete=models.CASCADE,null=True)
