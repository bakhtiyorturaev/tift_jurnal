from django import forms
from tinymce.widgets import TinyMCE
from .models import SampleDoc, CopyRight, ArticlePreparationGuide

class ArticlePreparationGuideForm(forms.ModelForm):
    class Meta:
        model = ArticlePreparationGuide
        fields = '__all__'
        widgets = {
            field: TinyMCE(attrs={'cols': 80, 'rows': 30})
            for field in ['yuriqnoma_uz', 'yuriqnoma_ru', 'yuriqnoma_en']
        }
class SampleDocForm(forms.ModelForm):
    content_uz = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label="Hujjat matni (UZ)")
    content_ru = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label="Hujjat matni (RU)", required=False)
    content_en = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label="Hujjat matni (EN)", required=False)

    class Meta:
        model = SampleDoc
        fields = '__all__'


class CopyRightForm(forms.ModelForm):
    content_uz = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label="Mualliflik huquqi matni (UZ)")
    content_ru = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label="Mualliflik huquqi matni (RU)", required=False)
    content_en = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label="Mualliflik huquqi matni (EN)", required=False)

    class Meta:
        model = CopyRight
        fields = '__all__'
