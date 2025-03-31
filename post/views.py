from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.models import User  # Importa el modelo User
from .models import Post  # Importa el modelo post
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'post/index.html')

@login_required
def categorias(request):
    return render(request, 'post/categorias.html')

@login_required
def publicaciones(request):
    if request.user.is_superuser or request.user.is_staff:
        posts = Post.objects.all().order_by('-created_at')  # Muestra todos los posts
    else:
        posts = Post.objects.filter(author=request.user).order_by('-created_at')  # Muestra solo los del usuario actual
    return render(request, 'post/publicaciones.html', {'posts': posts})

@login_required
def perfil(request):
    return render(request, 'post/perfil_usuario.html')

@login_required
def nueva_publicacion(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # No guarda aún en la BD
            post.author = request.user  # Asigna el usuario autenticado
            post.save()  # Guarda en la BD
            return redirect('publicaciones')  # Redirigir después de guardar
    else:
        form = PostForm()
    return render(request, 'post/nueva_publicacion.html', {'form': form})

@login_required
def editar_publicacion(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('publicaciones')
    else:
        form = PostForm(instance=post)
    return render(request, 'post/editar_publicacion.html', {'form': form})

@login_required
def eliminar_publicacion(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('publicaciones')
    return render(request, 'post/borrar_publicacion.html', {'post': post})