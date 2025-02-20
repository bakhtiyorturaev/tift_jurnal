from django.contrib import admin
from .forms import IlmiyMaktablarimForm
from .models import IlmiyMaktablarim


@admin.register(IlmiyMaktablarim)
class IlmiyMaktablarimAdmin(admin.ModelAdmin):
    form = IlmiyMaktablarimForm
    list_display = ['name', 'academic_degree_uz']
    search_fields = ['name', 'academic_degree_uz']

