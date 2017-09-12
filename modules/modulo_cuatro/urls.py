#Urls de app landing
from django.conf.urls import url
from .views import proyecto_final,update_user, registro, foro, add_comentario, add_respuesta, index, login, logout, exito, archivo_exito,  segunda_etapa, add_archivo
app_name = 'modulo_cuatro'
urlpatterns = [
    url(r'^registro/',registro, name="registro"),
    url(r'^update_user/',update_user, name="update_user"),
    url(r'^foro/$',foro, name="foro"),
    url(r'^add_comentario/$',add_comentario, name="add_comentario"),
    url(r'^add_respuesta/$',add_respuesta, name="add_respuesta"),
    url(r'^$',index, name="index"),
    url(r'^login/$',login, name="login"),
    url(r'^logout/$',logout, name="logout"),
    url(r'^exito/$',exito, name="exito"),
    url(r'^archivo_exito/$',archivo_exito, name="archivo_exito"),
    url(r'^segunda_etapa/$',segunda_etapa, name="segunda_etapa"),
    url(r'^add_archivo/$',add_archivo, name="add_archivo"),
    url(r'^proyecto_final/$',proyecto_final, name="proyecto_final"),


]