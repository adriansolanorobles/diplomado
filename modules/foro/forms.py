from django import forms
from django.forms import ModelForm
from .models import Comentario, Respuesta

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ('comentario_descripcion',)
        widgets = {
            'comentario_descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

class RespuestaForm(ModelForm):
    class Meta:
        model = Respuesta
        fields = ('respuesta_descripcion',)
        widgets = {
            'respuesta_descripcion': forms.Textarea(attrs={'class': 'form-control','rows':4, 'cols':15}),
        }