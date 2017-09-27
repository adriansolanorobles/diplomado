from django.contrib import admin
from .models import Archivo

class ArchivoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Archivo, ArchivoAdmin)