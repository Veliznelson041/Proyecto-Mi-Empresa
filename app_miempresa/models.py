from django.db import models

# Create your models here.

class Rubro(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de Rubro", unique=True)
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de Cliente")
    rubros = models.ForeignKey(Rubro, on_delete=models.PROTECT)
    email = models.EmailField(max_length=250, unique=True)
    imagen = models.ImageField(upload_to="clientes/", blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.nombre
    

 