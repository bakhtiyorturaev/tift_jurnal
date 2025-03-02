from django import forms
from tinymce.widgets import TinyMCE

from .models import AboutMagazine, MagazineRequirements

class AboutMagazineForm(forms.ModelForm):
    class Meta:
        model = AboutMagazine
        fields = '__all__'
        widgets = {
            field: TinyMCE(attrs={'cols': 80, 'rows': 30}) 
            for field in ['bio_uz', 'bio_ru', 'bio_en']
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Maydon mavjudligini tekshirib, help_text qo'shamiz
        if 'magazine_name_uz' in self.fields:
            self.fields['magazine_name_uz'].help_text = "✅ Bu maydon avtomatik ravishda tanlanadi."
        if 'magazine_name_ru' in self.fields:
            self.fields['magazine_name_ru'].help_text = "✅ Bu maydon avtomatik ravishda tanlanadi."
        if 'magazine_name_en' in self.fields:
            self.fields['magazine_name_en'].help_text = "✅ Bu maydon avtomatik ravishda tanlanadi."

class MagazineRequirementsForm(forms.ModelForm):
    content_uz = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label="Jurnal talablari to'liq (UZ)")
    content_ru = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label="Jurnal talablari to'liq (RU)", required=False)
    content_en = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label="Jurnal talablari to'liq (EN)", required=False)

    class Meta:
        model = MagazineRequirements
        fields = '__all__'

