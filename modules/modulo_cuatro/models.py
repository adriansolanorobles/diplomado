from django.db import models
from modules.users.models import User
from modules.etapas.models import Etapa
# Create your models here.

class ModuloCuatro(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    etapa = models.ForeignKey(Etapa,on_delete=models.CASCADE)
    activo = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.activo)