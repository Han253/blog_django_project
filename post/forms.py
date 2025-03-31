from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post  
        fields = ['title', 'content', 'category', 'published']  
        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'category': 'Categoría',
            'published': '¿Publicar ahora?',
        }
        widgets = {
            'title': forms.TextInput(attrs={'id': 'title'}),
            'content': forms.Textarea(attrs={'id': 'content', 'rows': 5}),
            'category': forms.Select(attrs={'id': 'category'}),
            'published': forms.CheckboxInput(attrs={'id': 'published'}),
        }
