from django.contrib import admin
from .models import ModuloCuatro

class ModuloCuatroAdmin(admin.ModelAdmin):
    pass
admin.site.register(ModuloCuatro, ModuloCuatroAdmin)