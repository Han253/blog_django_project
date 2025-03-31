from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'post/index.html')

def categorias(request):
    return render(request, 'post/categorias.html')

def publicaciones(request):
    return render(request, 'post/publicaciones.html')

def perfil(request):
    return render(request, 'post/perfil_usuario.html')
