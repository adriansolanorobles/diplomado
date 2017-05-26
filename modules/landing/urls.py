#Urls de app landing
from django.conf.urls import url
from .views import index, index_get_template
app_name = 'landing'
urlpatterns = [
    url(r'^$',index, name="index"),
    url(r'^(?P<page>[\w]+)/$',index_get_template, name="index_get_template"),
    
]