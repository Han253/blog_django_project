from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categorias/', views.categorias, name='categorias'),
    path('publicaciones/', views.publicaciones, name='publicaciones'),
    path('perfil', views.perfil, name='perfil'),
    path('publicaciones/nueva/', views.nueva_publicacion, name='nueva_publicacion'),
    path('publicaciones/editar/<int:post_id>/', views.editar_publicacion, name='editar_publicacion'),
    path('publicaciones/eliminar/<int:post_id>/', views.eliminar_publicacion, name='eliminar_publicacion'),
]