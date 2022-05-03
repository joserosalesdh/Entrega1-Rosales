from django import forms


class FormBlog(forms.Form):
    titulo = forms.CharField(max_length=200)
    subtitulo = forms.CharField(max_length=200)
    # fechaPublicacion = forms.DateField()
    pais = forms.CharField(max_length=200)
    ciudad = forms.CharField(max_length=200)
    contenido = forms.CharField(widget=forms.Textarea)
    autor = forms.CharField(max_length=200)


class FormLibro(forms.Form):
    titulo = forms.CharField(max_length=200)
    # fechaPublicacion = forms.DateField()
    breveDescripcion = forms.CharField(widget=forms.Textarea)
    autor = forms.CharField(max_length=200)
    precio = forms.IntegerField()


class FormAutor(forms.Form):
    nombre = forms.CharField(max_length=200)
    apellido = forms.CharField(max_length=200)
    # fechaNacimiento = forms.DateField()
    pais = forms.CharField(max_length=200)
    ciudad = forms.CharField(max_length=200)
    historia = forms.CharField(widget=forms.Textarea)
    profesion = forms.CharField(max_length=200)
