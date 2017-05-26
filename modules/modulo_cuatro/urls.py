#Urls de app landing
from django.conf.urls import url
from .views import registro, foro, add_comentario, add_respuesta, index, login, logout, exito
app_name = 'modulo_cuatro'
urlpatterns = [
    url(r'^registro/$',registro, name="registro"),
    url(r'^foro/$',foro, name="foro"),
    url(r'^add_comentario/$',add_comentario, name="add_comentario"),
    url(r'^add_respuesta/$',add_respuesta, name="add_respuesta"),
    url(r'^$',index, name="index"),
    url(r'^login/$',login, name="login"),
    url(r'^logout/$',logout, name="logout"),
    url(r'^exito/$',exito, name="exito"),
]