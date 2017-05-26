from django.db import models

# Create your models here.

class Etapa(models.Model):
    descripcion = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
