from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Name')
    INSTRUMENT_CHOICES = [
        ('guitar', 'Guitar'),
        ('piano', 'Piano'),
    ]
    instrument = models.CharField(max_length=255, choices=INSTRUMENT_CHOICES, verbose_name='Instrument')
    
    GENRE_CHOICES = [
        ('rock', 'Rock'),
        ('jazz', 'Jazz'),
    ]
    genre = models.CharField(max_length=255, choices=GENRE_CHOICES, verbose_name='Genre')
    users = models.ManyToManyField('UserProfile', related_name='songs', blank=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    liked_songs = models.ManyToManyField('Song', related_name='liked_by', blank=True)
    learned_songs = models.ManyToManyField('Song', related_name='learned_by', blank=True)
    bio = models.TextField(blank=True, verbose_name='Bio')

    def __str__(self):
        return self.user.username