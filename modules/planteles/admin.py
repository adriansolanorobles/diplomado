from django.contrib import admin
from .models import Plantel

class PlantelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Plantel, PlantelAdmin)