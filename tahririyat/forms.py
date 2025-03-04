from django import forms
from tinymce.widgets import TinyMCE
from .models import EditorialStaff

class EditorialStaffForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = EditorialStaff
        fields = '__all__'
        widgets = {
            field: TinyMCE(attrs={'cols': 80, 'rows': 30})
            for field in ['content_uz', 'content_ru', 'content_en']
        }



