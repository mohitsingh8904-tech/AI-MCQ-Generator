from django import forms
from .models import UploadedNotes

class UploadNotesForm(forms.ModelForm):
    class Meta:
        model = UploadedNotes
        fields = ["file"]
