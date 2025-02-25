from django import forms
from tinymce.widgets import TinyMCE
from .models import EditorialStaff

class EditorialStaffForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label="Tahririyat a'zolari ro'yxati (UZ)")

    class Meta:
        model = EditorialStaff
        fields = '__all__'



