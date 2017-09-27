from django.db import models
from modules.users.models import User
from modules.etapas.models import Etapa
import time

def content_file_name(instance, filename):
	    ext = filename.split('.')[-1]
	    filename = "%s.%s" % (str(int(round(time.time()*1000))), ext)
	    return os.path.join('archivos/', filename)
# Create your models here.
class Archivo(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    upload = models.FileField(upload_to=content_file_name)
    upload_calificado = models.FileField(upload_to=content_file_name, null=True,blank=True)
    etapa = models.ForeignKey(Etapa,on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.upload) 
    