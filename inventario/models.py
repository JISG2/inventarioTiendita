from django.db import models

# Create your models here.
class proteinasModel(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    precio = models.FloatField(max_length=100)
    gramos = models.FloatField(max_length=100)
    marca = models.CharField(max_length=50)
    carbohidratos = models.FloatField(max_length=50)
    servicios = models.IntegerField()
    gramosProteinas = models.FloatField(max_length=40)
    urlImagen = models.CharField(max_length=255)

class aminoacidosModel(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    precio = models.FloatField(max_length=100)
    marca = models.CharField(max_length=50)
    cantidadServicios = models.IntegerField()
    presentacion = models.CharField(max_length=50)
    urlImagen = models.CharField(max_length=255)

class glutaminasModel(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    precio = models.FloatField(max_length=100)
    marca = models.CharField(max_length=50)
    presentacion = models.CharField(max_length=50)
    urlImagen = models.CharField(max_length=255)
    