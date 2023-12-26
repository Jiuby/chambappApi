from django.db import models

# Create your models here.
class chambeador(models.Model):
    Nombre = models.CharField(max_length=50)
    NombreEspecial = models.CharField(max_length=50)
    Servicio = models.CharField(max_length=50)
    Precio = models.CharField(max_length=50)
    Contacto = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre + ' ' + self.NombreEspecial