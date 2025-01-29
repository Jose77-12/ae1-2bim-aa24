from django.db import models  # type: ignore

# Create your models here.


class PlatosTipicosDeEcuador(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
