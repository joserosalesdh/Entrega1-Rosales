from django.shortcuts import render, redirect
from django.http import HttpResponse

from blogs.models import Autor, Blog, Libro
from .forms import FormAutor, FormBlog, FormLibro


def inicio(request):
    return HttpResponse("Aca va la pagina de inicio")


def buscar_blog(request, pais):
    if request.GET.get("titulo"):
        titulo = request.GET.get("titulo")
        blogs = Blog.objects.filter(titulo__icontains=titulo, pais=pais)
        return render(request, "blogs/resultadoBuscarBlog.html", {"blogs": blogs})

    return render(request, "blogs/buscarBlog.html")


def nuevo_blog(request):
    if request.method == "POST":
        mi_form = FormBlog(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            blog = Blog(
                titulo=info["titulo"],
                subtitulo=info["subtitulo"],
                # fechaPublicacion=info["fechaPublicacion"],
                pais=info["pais"],
                ciudad=info["ciudad"],
                contenido=info["contenido"],
                autor=info["autor"]
            )
            blog.save()
            return redirect("InicioBlogs")

    mi_form = FormBlog()

    return render(request, "blogs/formBlogs.html", {"form": mi_form})


def nuevo_libro(request):
    if request.method == "POST":
        mi_form = FormLibro(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            libro = Libro(
                titulo=info["titulo"],
                # fechaPublicacion=info["fechaPublicacion"],
                breveDescripcion=info["breveDescripcion"],
                autor=info["autor"],
                precio=info["precio"]
            )
            libro.save()
            return redirect("InicioBlogs")

    mi_form = FormLibro()

    return render(request, "blogs/formLibros.html", {"form": mi_form})


def nuevo_autor(request):
    if request.method == "POST":
        mi_form = FormAutor(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            autor = Autor(
                nombre=info["nombre"],
                apellido=info["apellido"],
                # fechaNacimiento=info["fechaNacimiento"],
                pais=info["pais"],
                ciudad=info["ciudad"],
                historia=info["historia"],
                profesion=info["profesion"]
            )
            autor.save()
            return redirect("InicioBlogs")

    mi_form = FormAutor()
    return render(request, "blogs/formAutores.html", {"form": mi_form})
