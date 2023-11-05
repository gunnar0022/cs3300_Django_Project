from django import forms
from .models import Song

class SongAddForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'instrument', 'genre']

class SongEditForm(SongAddForm):
    pass

class SongDeleteForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = []
