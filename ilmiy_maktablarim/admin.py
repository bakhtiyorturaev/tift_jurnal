from django import forms
from django.contrib import admin
from .models import IlmiyMaktablarim
from tinymce.widgets import TinyMCE

class IlmiyMaktablarimForm(forms.ModelForm):
    haqida = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = IlmiyMaktablarim
        fields = '__all__'

@admin.register(IlmiyMaktablarim)
class IlmiyMaktablarimAdmin(admin.ModelAdmin):
    form = IlmiyMaktablarimForm
    list_display = ['name', 'academic_degree']
    search_fields = ['name', 'academic_degree']

