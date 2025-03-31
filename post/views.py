from django.shortcuts import render,redirect
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User  # Importa el modelo User
from .models import Post, Category  # Importar modelo post, y Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


# Create your views here.

def index(request):
    publicaciones_recientes = Post.objects.all().order_by('-created_at')[:6]  # Últimas 6 publicaciones
    return render(request, 'post/index.html',{'publicaciones_recientes': publicaciones_recientes})

@login_required
def categorias(request):
    categorias = Category.objects.all()
    categoria_id = request.GET.get('categoria')  # Capturar la categoría seleccionada
    publicaciones = Post.objects.all().order_by('-created_at')
    
    if categoria_id:
        categoria = get_object_or_404(Category, id=categoria_id)
        publicaciones = publicaciones.filter(category=categoria)        

    return render(request, 'post/categorias.html', {
        'categorias': categorias,
        'publicaciones': publicaciones,
        'categoria_seleccionada': categoria_id
    })

@login_required
def publicaciones(request):
    if request.user.is_superuser or request.user.is_staff:
        posts = Post.objects.all().order_by('-created_at')  # Muestra todos los posts
    else:
        posts = Post.objects.filter(author=request.user).order_by('-created_at')  # Muestra solo los del usuario actual
    return render(request, 'post/publicaciones.html', {'posts': posts})

@login_required
def perfil(request):
    return render(request, 'post/perfil_usuario.html', {'usuario': request.user})

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


def detalle_publicacion(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = post.comments.all().order_by('-created_at')  # Trae todos los comentarios ordenados por fecha
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.author = request.user  # Se asigna el usuario autenticado
            comentario.save()
            return redirect('detalle_publicacion', post_id=post.id)

    return render(request, 'post/detalle_publicacion.html', {
        'post': post,
        'comentarios': comentarios,
        'form': form
    })
