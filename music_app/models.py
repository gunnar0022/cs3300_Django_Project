from django.db import models
from django.db import models

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
    users = models.ManyToManyField('User', related_name='songs', blank=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    email = models.EmailField(unique=True, verbose_name='Email')
    bio = models.TextField(blank=True, verbose_name='Bio')

    def __str__(self):
        return self.name
