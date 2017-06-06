from django.db import models
from modules.users.models import User
from modules.etapas.models import Etapa

# Create your models here.
class Archivo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    upload = models.FileField(upload_to='archivos/')
    etapa = models.ForeignKey(Etapa,on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.upload) 