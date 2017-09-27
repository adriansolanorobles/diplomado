from django.contrib import admin
from .models import Archivo

class ArchivoAdmin(admin.ModelAdmin):
	list_display = ('user', 'upload', 'upload_calificado')
	
admin.site.register(Archivo, ArchivoAdmin)