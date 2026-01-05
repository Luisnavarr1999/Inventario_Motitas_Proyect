from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer
from .filters import ProductoFilter

class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all().order_by("-id")
    serializer_class = ProductoSerializer

    filterset_class = ProductoFilter
    search_fields = ["nombre"]
    ordering_fields = ["id", "nombre", "precio", "stock", "creado_en"]


class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

