from django import forms
from django.forms import ModelForm


class LoginForm(forms.Form):

    email = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Correo electrónico"
        }
    )) 
    
    password  = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Contraseña"
            }
        ))