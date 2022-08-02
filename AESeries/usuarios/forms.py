from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormCritico(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    alias = forms.CharField(max_length=20)
    experiencia = forms.CharField(widget=forms.Textarea)


class FormBinger(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    alias = forms.CharField(max_length=20)


class FormRegistro(UserCreationForm):

    email = forms.EmailField()
    password1: forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2: forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]