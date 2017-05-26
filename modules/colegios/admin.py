from django.contrib import admin
from .models import Colegio

class ColegioAdmin(admin.ModelAdmin):
    pass
admin.site.register(Colegio, ColegioAdmin)