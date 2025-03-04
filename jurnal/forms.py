from django import forms
from tinymce.widgets import TinyMCE

from .models import AboutMagazine, MagazineRequirements, MagazineNews

class AboutMagazineForm(forms.ModelForm):
    class Meta:
        model = AboutMagazine
        fields = '__all__'
        widgets = {
            field: TinyMCE(attrs={'cols': 80, 'rows': 30}) 
            for field in ['bio_uz', 'bio_ru', 'bio_en']
        }

# class MagazineRequirementsForm(forms.ModelForm):
#     content_uz = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label="Jurnal talablari to'liq (UZ)")
#     content_ru = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label="Jurnal talablari to'liq (RU)",
#                                  required=False)
#     content_en = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label="Jurnal talablari to'liq (EN)",
#                                  required=False)
#
#     class Meta:
#         model = MagazineRequirements
#         fields = '__all__'

class MagazineNewsForm(forms.ModelForm):
    class Meta:
        model = MagazineNews
        fields = '__all__'
        widgets = {
            field: TinyMCE(attrs={'cols': 80, 'rows': 35})
            for field in ['content_uz', 'content_ru', 'content_en', 'content_uz', 'content_ru', 'content_en']
        }