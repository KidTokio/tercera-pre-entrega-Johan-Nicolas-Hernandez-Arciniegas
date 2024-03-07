from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20, default="")
    email = models.EmailField()
    numero = models.IntegerField()
    direccion = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField()
    clave = models.CharField(max_length=20)
    numero = models.IntegerField()
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} || {self.email}"

class Articulo(models.Model):
    nombre = models.CharField(max_length=20)
    selectorCategoria = [
                        ("polera", "Polera"),
                        ("hoodie", "Hoodie"),
                        ("sueter", "Sueter"),
                        ("pantalon", "Pantalon"),
                        ("gorro", "Gorro"),
                        ("accesorio", "Accesorio")
                        ]
    categoria = models.CharField(max_length=20, choices=selectorCategoria, default="polera")
    precio = models.IntegerField()
    disponibilidad = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} ${self.precio} || {self.categoria} ||{self.disponibilidad}"