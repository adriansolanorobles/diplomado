from django.db import models
from modules.users.models import User

# Create your models here.
class Archivo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    upload = models.FileField(upload_to='media/')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True) 