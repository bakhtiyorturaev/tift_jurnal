from django import forms
from .models import Conference
from tinymce.widgets import TinyMCE

class ConferenceForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Conference
        fields = "__all__"

