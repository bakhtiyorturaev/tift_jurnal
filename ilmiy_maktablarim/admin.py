from django.contrib import admin
from django_ckeditor_5.fields import CKEditor5Field

from .models import IlmiyMaktablarim
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms

class IlmiyMaktablarimAdminForm(forms.ModelForm):

    class Meta:
        model = IlmiyMaktablarim
        fields = '__all__'
        widgets = {
            "bio": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name='extends'
            )
        }

@admin.register(IlmiyMaktablarim)
class IlmiyMaktablarimAdmin(admin.ModelAdmin):
    form = IlmiyMaktablarimAdminForm
    list_display = ['name', 'academic_degree']
    search_fields = ['name', 'academic_degree']
    formfield_overrides = {
        CKEditor5Field: {'widget': CKEditor5Widget(config_name='extends')},  # Kengaytirilgan CKEditor toolbarni qo'llash
    }
