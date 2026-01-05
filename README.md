# Inventario Motitas API (Proyecto de práctica)

Este proyecto es una **API REST de inventario** construida con Django REST Framework. Fue creada únicamente para **practicar el desarrollo de APIs**, incluyendo autenticación JWT, filtrado, paginación y documentación auto-generada.

## Tecnologías principales

- Django 6 y Django REST Framework
- django-filter para filtros declarativos
- djangorestframework-simplejwt para autenticación con tokens JWT
- drf-spectacular para la generación de la documentación OpenAPI/Swagger

## Puesta en marcha rápida

1. Crea y activa un entorno virtual de Python.
2. Instala las dependencias: `pip install -r requirements.txt`.
3. Aplica las migraciones: `python manage.py migrate`.
4. (Opcional) Crea un superusuario para probar desde el panel de administración: `python manage.py createsuperuser`.
5. Ejecuta el servidor: `python manage.py runserver`.

> Nota: para ejecutar en local añade tu host (por ejemplo `127.0.0.1`) a `ALLOWED_HOSTS` en `config/settings.py`, ya que la configuración actual apunta a un despliegue de prueba.

## Endpoints principales

- Autenticación JWT: `POST /api/token/` (obtener) y `POST /api/token/refresh/` (refrescar).
- Productos: `GET/POST /api/productos/` y `GET/PATCH/PUT/DELETE /api/productos/<id>/`.
  - Filtros: `min_precio`, `max_precio`, `categoria`, `activo`.
  - Búsqueda: `?search=<texto>` sobre el nombre.
  - Ordenación: `?ordering=id|nombre|precio|stock|creado_en` (usa `-` para descendente).
- Categorías: `GET/POST /api/categorias/` y `GET/PATCH/PUT/DELETE /api/categorias/<id>/`.
- Documentación interactiva: Swagger UI en `GET /api/docs/` (usa el esquema `GET /api/schema/`).

## Propósito del repositorio

El código no está pensado para producción; su meta es servir como material de práctica para construir, asegurar y documentar una API REST con Django.