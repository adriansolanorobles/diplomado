from django import forms
from django.forms import ModelForm
from .models import Archivo

class ArchivoForm(ModelForm):
    class Meta:
        model = Archivo
        fields = ('upload',)
        widgets = {
            'upload': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'accept': '.docx,.pdf'
                    }
                ),
        }

