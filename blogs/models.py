from django.db import models


class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    # fechaPublicacion = models.DateField()
    pais = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.CharField(max_length=200)

    # def __str__(self):
    #     return f"[{self.tema}] {self.titulo}"


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    # fechaPublicacion = models.DateField()
    breveDescripcion = models.TextField()
    autor = models.CharField(max_length=200)
    precio = models.IntegerField()


class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    # fechaNacimiento = models.DateField()
    pais = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    historia = models.TextField()
    profesion = models.CharField(max_length=200)
