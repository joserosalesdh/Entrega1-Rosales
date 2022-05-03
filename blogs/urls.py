from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="InicioBlogs"),
    path("nuevo_blog", views.nuevo_blog, name="NuevoBlog"),
    path("nuevo_libro", views.nuevo_libro, name="NuevoLibro"),
    path("nuevo_autor", views.nuevo_autor, name="NuevoAutor"),
    path("buscar/<pais>", views.buscar_blog, name="BuscarBlogs")
    # path("buscar/resultados", views.inicio, name="BuscarBlogs")
    # path("buscar/<titulo>", views.inicio, name="BuscarLibro")
    # path("buscar/<titulo>", views.inicio, name="BuscarAutor")
]
