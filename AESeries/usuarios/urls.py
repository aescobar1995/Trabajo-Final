from django.urls import path
from . import views

urlpatterns = [
    path("criticos", views.criticos, name="ListaCriticos"),
    path("nuevo_critico", views.nuevo_critico, name="NuevoCritico"),
    path("critico/<id>", views.ver_critico, name="VerCritico"),
    path("critico/editar/<id>", views.mod_critico, name="EditarCritico"),
    path("critico/eliminar/<id>", views.del_critico, name="EliminarCritico"),
    
    path("bingers", views.bingers, name="ListaBingers"),
    path("buscarbinger", views.buscarBinger, name="BuscarBinger"),
    path("buscar/", views.buscarB, name="BuscarB"),
    path("nuevo_binger", views.nuevo_binger, name="NuevoBinger"),
    path("binger/<id>", views.ver_bingers, name="VerBinger"),
    path("binger/editar/<id>", views.mod_binger, name="EditarBinger"),
    path("binger/eliminar/<id>", views.del_binger, name="EliminarBinger"),

    path("registro", views.register, name="Register"),
    path("editaruser", views.mod_Usuario, name="EditarUsuario"),

]