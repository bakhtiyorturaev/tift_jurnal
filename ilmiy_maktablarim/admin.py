from django.contrib import admin
from .models import IlmiyMaktablarim

@admin.register(IlmiyMaktablarim)
class IlmiyMaktablarimAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
