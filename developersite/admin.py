from django.contrib import admin

from .models import Developer

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('user', 'g_plus', 'contact', 'profile')

admin.site.register(Developer)
