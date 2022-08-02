from django.shortcuts import render, redirect
import django
from usuarios.models import Critico, Binger
from .forms import FormCritico, FormBinger, FormRegistro
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from urllib import request
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':

        regform = FormRegistro(request.POST)
        if regform.is_valid():
            username=regform.cleaned_data['username']
            regform.save()
        return render(request, 'paginas/inicio.html', {'mensaje':"Usuario Creado"})

    else:
        regform = FormRegistro()

    return render(request, 'usuarios/registro.html', {'form':regform})

def admin_o_ususario(user):
    if not user.is_authenticated:
        return False
    if user.is_staff:
        return True 
    try:
        user = user.objects.get(usuario=user.id)
    except ObjectDoesNotExist:
        user = None

    return user is not None

def es_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(es_admin)
def mod_Usuario(request):

    usuario = request.user

    if request.method == "POST":
        mi_form = FormRegistro(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            usuario.username = info["username"]
            usuario.email = info["email"]
            usuario.password1 = info["password1"]
            usuario.password2 = info["password2"]
            usuario.save()
            return redirect("Inicio")

    mi_form = FormRegistro(
        initial={
            "username": usuario.username,
            "email": usuario.email,
        }
    )

    return render(request, "usuarios/formUsuario.html", {"Userform": mi_form, 'usuario':usuario.username})


def bingers(request):
    user = Binger.objects.all()
    return render(request, "usuarios/bingers.html", {"bingers": user})


def ver_bingers(request, id):
    user = Binger.objects.get(id=id)
    return render(request, "usuarios/ver_binger.html", {"binger": user})

@user_passes_test(es_admin)
def nuevo_binger(request):
    if request.method == "POST":
        mi_form = FormBinger(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            user = Binger(
                nombre=info["nombre"],
                apellido=info["apellido"],
                email=info["email"],
                alias=info["alias"],
            )
            user.save()
            return redirect("ListaBingers")

    mi_form = FormBinger()

    return render(request, "usuarios/formBingers.html", {"Bingerform": mi_form})

@user_passes_test(es_admin)
def mod_binger(request, id):
    user = Binger.objects.get(id=id)

    if request.method == "POST":
        mi_form = FormBinger(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            user.nombre = info["nombre"]
            user.apellido = info["apellido"]
            user.email = info["email"]
            user.alias = info["alias"]

            user.save()
            return redirect("ListaBingers")

    mi_form = FormBinger(
        initial={
            "nombre": user.nombre,
            "apellido": user.apellido,
            "email": user.email,
            "alias": user.alias,
        }
    )

    return render(request, "usuarios/formBingers.html", {"Bingerform": mi_form})

@user_passes_test(es_admin)
def del_binger(request, id):
    user = Binger.objects.get(id=id)

    user.delete()
    return redirect("ListaBingers")



def buscarBinger(request):
    return render(request, "usuarios/buscarBinger.html")
    #return redirect("buscarBinger")

def buscarB(request):
    if request.GET.get("nombre"):                                           
        nombre = request.GET.get("nombre")                                 
        user = Binger.objects.filter(nombre__icontains=nombre)                            
        return render(request, "usuarios/busquedaB.html", {"user": user}) 

    #return render(request, "usuarios/buscarBinger.html")


def criticos(request):
    critico = Critico.objects.all()

    return render(request, "usuarios/criticos.html", {"criticos": critico})

@user_passes_test(es_admin)
def ver_critico(request, id):
    critic = Critico.objects.get(id=id)
    return render(request, "usuarios/ver_critico.html", {"critico": critic})

@user_passes_test(es_admin)
def mod_critico(request, id):
    critic = Critico.objects.get(id=id)

    if request.method == "POST":
        mi_form = FormCritico(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            critic.nombre = info["nombre"]
            critic.apellido = info["apellido"]
            critic.email = info["email"]
            critic.alias = info["alias"]
            critic.experiencia = info["experiencia"]

            critic.save()
            return redirect("ListaCriticos")

    mi_form = FormCritico(
        initial={
            "nombre": critic.nombre,
            "apellido": critic.apellido,
            "email": critic.email,
            "alias": critic.alias,
            "experiencia": critic.experiencia,
        }
    )

    return render(request, "usuarios/formCriticos.html", {"Criticform": mi_form})

@user_passes_test(es_admin)
def nuevo_critico(request):
    if request.method == "POST":
        mi_form = FormCritico(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            critic = Critico(
                nombre=info["nombre"],
                apellido=info["apellido"],
                email=info["email"],
                alias=info["alias"],
                experiencia=info["experiencia"],
            )
            critic.save()
            return redirect("ListaCriticos")

    mi_form = FormCritico()

    return render(request, "usuarios/formCriticos.html", {"Criticform": mi_form})

@user_passes_test(es_admin)
def del_critico(request, id):
    critic = Critico.objects.get(id=id)

    critic.delete()
    return redirect("ListaCriticos")