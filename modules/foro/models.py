from django.db import models
from modules.users.models import User

# Create your models here.

class Comentario(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comentario_descripcion = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.comentario_descripcion)

class Respuesta(models.Model):
    comentario = models.ForeignKey(Comentario,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    respuesta_descripcion = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.respuesta_descripcion)