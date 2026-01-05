from django.urls import path
from .views import ProductoListCreateView, ProductoDetailView, CategoriaListCreateView, CategoriaDetailView

urlpatterns = [
    path("productos/", ProductoListCreateView.as_view(), name="productos-list-create"),
    path("productos/<int:pk>/", ProductoDetailView.as_view(), name="producto-detail"),

    path("categorias/", CategoriaListCreateView.as_view(), name="categorias-list-create"),
    path("categorias/<int:pk>/", CategoriaDetailView.as_view(), name="categoria-detail"),
]
