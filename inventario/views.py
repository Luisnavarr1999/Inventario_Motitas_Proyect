from rest_framework import generics
from .models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer
from .filters import ProductoFilter

class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all().order_by("nombre")
    serializer_class = CategoriaSerializer

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all().order_by("-id")
    serializer_class = ProductoSerializer

    filterset_class = ProductoFilter
    search_fields = ["nombre"]
    ordering_fields = ["id", "nombre", "precio", "stock", "creado_en"]

class ProductoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

