from django.db import models
from django.db.models import Q

class Categoria(models.Model):
    nombre = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="productos",
        null=True,
        blank=True,
    )
    nombre = models.CharField(max_length=120)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creado_en"]
        constraints = [
            models.CheckConstraint(condition=Q(precio__gt=0), name="precio_mayor_que_cero"),
            models.CheckConstraint(condition=Q(stock__gte=0), name="stock_no_negativo"),
            models.UniqueConstraint(fields=["categoria", "nombre"], name="unique_producto_por_categoria"),
        ]



    def __str__(self):
        return self.nombre
