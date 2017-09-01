from django import forms
from django.forms import ModelForm
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('nombre','apellido_paterno','apellido_materno','telefono',)
        widgets = {
            'nombre': forms.TextInput(attrs=
                    {
                        "class": "form-control",
                        
                    }
                ),
            'apellido_paterno': forms.TextInput(attrs=
                    {
                        'class': 'form-control',
                        
                    }
                ),
            'apellido_materno': forms.TextInput(attrs=
                    {
                        'class': 'form-control',
                        
                    }
                ),

            'telefono': forms.TextInput(attrs={'class': 'form-control'}),            
        }