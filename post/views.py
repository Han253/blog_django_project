from django.shortcuts import render,redirect
from .forms import PostForm
from django.contrib.auth.models import User  # Importa el modelo User
from .models import Post  # Importar modelo post


# Create your views here.

def index(request):
    return render(request, 'post/index.html')

def categorias(request):
    return render(request, 'post/categorias.html')

def publicaciones(request):
    posts = Post.objects.all().order_by('-created_at')  # Ordenados por fecha de creación
    return render(request, 'post/publicaciones.html', {'posts': posts})

def perfil(request):
    return render(request, 'post/perfil_usuario.html')

def nueva_publicacion(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # No guarda aún en la BD
            post.author = User.objects.get(id=1)  # Asigna el usuario con ID 1
            post.save()  # Guarda en la BD
            return redirect('publicaciones')  # Redirigir después de guardar
    else:
        form = PostForm()
    return render(request, 'post/nueva_publicacion.html', {'form': form})
