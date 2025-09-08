from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': '30', 'cols': '120', 'placeholder': 'Enter your note here', 'style': 'background-color: #181818; color: #aaaaaa; border: #aaaaaa; border-width: 4px; border-style: solid; border-radius: 5px; outline: none; padding: 10px;'}),
        }
        labels = {
            'text': '',
        }
