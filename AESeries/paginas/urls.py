from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("about", views.sobremi, name="About"),

    path("buscarserie", views.buscarSerie, name="BuscarSerie"),
    path("buscar/", views.buscarS, name="BuscarS"),
    path("serie/<codserie>", views.ver_serie, name="VerSerie"),
    path("nueva_serie", views.nueva_serie, name="NuevaSerie"),
    path("login", views.login_request, name="Login"),
    path("logout", LogoutView.as_view(template_name='paginas/logout.html'), name="Logout"),
    
    #CBV con expresiones regulares (regular expression)
    path("series", views.SerieList.as_view(), name="SerieList"),
    re_path(r'^borrar/(?P<pk>\d+)$', views.SerieDelete.as_view(), name='Delete'),
    re_path(r'^editar/(?P<pk>\d+)$', views.SerieUpdate.as_view(), name='Edit'),    
]