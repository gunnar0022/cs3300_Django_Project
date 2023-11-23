from django import forms
from .models import Song
from .models import Rating


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


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['enjoyment', 'difficulty', 'comments']