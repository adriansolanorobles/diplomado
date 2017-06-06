from django.db import models

# Create your models here.

class Etapa(models.Model):
    descripcion = models.CharField(max_length=250)
    estatus = models.CharField(max_length=250)
    orden = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.orden) +' '+ self.descripcion + ' ' + self.estatus
