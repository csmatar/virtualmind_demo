from django.contrib import admin

from .models import Core

class CoreAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Core, CoreAdmin)