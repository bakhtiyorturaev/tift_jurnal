from tinymce.widgets import TinyMCE
from ilmiy_maktablarim.models import IlmiyMaktablarim
from django import forms

class IlmiyMaktablarimForm(forms.ModelForm):
    class Meta:
        model = IlmiyMaktablarim
        fields = '__all__'
        widgets = {
            field: TinyMCE(attrs={'cols': 80, 'rows': 30})
            for field in ['haqida_uz', 'haqida_ru', 'haqida_en']
        }
