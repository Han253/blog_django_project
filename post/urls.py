from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categorias/', views.categorias, name='categorias'),
    path('publicaciones/', views.publicaciones, name='publicaciones'),
    path('perfil/', views.perfil, name='perfil'),
    path('publicaciones/nueva/', views.nueva_publicacion, name='nueva_publicacion'),
]