from rest_framework import serializers
from .models import Producto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["id", "nombre"]

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(
        source="categoria",
        queryset=Categoria.objects.all(),
        write_only=True,
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Producto
        fields = [
            "id", "nombre", "precio", "stock", "activo", "creado_en",
            "categoria", "categoria_id"
        ]
        read_only_fields = ["id", "creado_en"]

    def validate_nombre(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("El nombre no puede estar vacío.")
        return value

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser mayor que 0.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("El stock no puede ser negativo.")
        return value

    def validate(self, attrs):
        activo = attrs.get("activo", getattr(self.instance, "activo", True))
        stock = attrs.get("stock", getattr(self.instance, "stock", 0))

        if activo is False and stock > 0:
            raise serializers.ValidationError("Si el producto está inactivo, el stock debe ser 0.")

        # Unicidad por categoría (mensaje bonito)
        categoria = attrs.get("categoria", getattr(self.instance, "categoria", None))
        nombre = attrs.get("nombre", getattr(self.instance, "nombre", "")).strip()

        if categoria and nombre:
            qs = Producto.objects.filter(categoria=categoria, nombre__iexact=nombre)
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise serializers.ValidationError("Ya existe un producto con ese nombre en esta categoría.")

        return attrs

