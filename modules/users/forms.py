from django import forms
from django.forms import ModelForm
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('nombre','apellido_paterno','apellido_materno','telefono','sexo')
        widgets = {
            'nombre': forms.TextInput(attrs=
                    {
                        "class": "form-control",
                        "pattern":"^([a-zA-Z]+(?:\.)?(?:(?:'| )[a-zA-Z]+(?:\.)?)*)$",
                    }
                ),
            'apellido_paterno': forms.TextInput(attrs=
                    {
                        'class': 'form-control',
                        "pattern":"^([a-zA-Z]+(?:\.)?(?:(?:'| )[a-zA-Z]+(?:\.)?)*)$",
                    }
                ),
            'apellido_materno': forms.TextInput(attrs=
                    {
                        'class': 'form-control',
                        "pattern":"^([a-zA-Z]+(?:\.)?(?:(?:'| )[a-zA-Z]+(?:\.)?)*)$",
                    }
                ),

            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'},choices=(('M', 'Mujer'), ('H', 'Hombre'))),
        }