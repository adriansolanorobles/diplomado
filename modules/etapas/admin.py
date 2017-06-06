from django.contrib import admin
from .models import Etapa

class EtapaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Etapa, EtapaAdmin)