import django_filters
from .models import Producto

class ProductoFilter(django_filters.FilterSet):
    min_precio = django_filters.NumberFilter(
        field_name="precio", lookup_expr="gte"
    )
    max_precio = django_filters.NumberFilter(
        field_name="precio", lookup_expr="lte"
    )

    class Meta:
        model = Producto
        fields = ["activo"]
