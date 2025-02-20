from django import forms
from tinymce.widgets import TinyMCE

from .models import AboutMagazine, MagazineRequirements, MagazineArchive

class AboutMagazineForm(forms.ModelForm):
    class Meta:
        model = AboutMagazine
        fields = '__all__'
        widgets = {
            field: TinyMCE(attrs={'cols': 80, 'rows': 30}) 
            for field in ['bio_uz', 'bio_ru', 'bio_en']
        }

class MagazineRequirementsForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = MagazineRequirements
        fields = '__all__'
        labels = {
            'content': 'Jurnal talablari to\'liq'
        }

class MagazineArchiveForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = MagazineArchive
        fields = '__all__'
        labels = {
            'content': 'Arxiv'
        }

