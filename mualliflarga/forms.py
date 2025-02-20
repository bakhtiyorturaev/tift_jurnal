from django import forms
from tinymce.widgets import TinyMCE
from .models import SampleDoc, CopyRight

class SampleDocForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = SampleDoc
        fields = '__all__'
        labels = {
            'content': 'Hujjat matni'
        }

class CopyRightForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = CopyRight
        fields = '__all__'
        labels = {
            'content': 'Mualliflik huquqi'
        }