from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
