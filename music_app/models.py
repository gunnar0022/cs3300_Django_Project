from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Song(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Name')
    INSTRUMENT_CHOICES = [
        ('guitar', 'Guitar'),
        ('drums', 'Drums'),
        ('violin', 'Violin'),
        ('flute', 'Flute'),
        ('cello', 'Cello'),

    ]
    instrument = models.CharField(max_length=255, choices=INSTRUMENT_CHOICES, verbose_name='Instrument')
    
    GENRE_CHOICES = [
        ('rock', 'Rock'),
        ('jazz', 'Jazz'),
        ('pop', 'Pop'),
        ('hip_hop', 'Hip Hop'),
        ('edm', 'EDM'),
        ('classical', 'Classical'),
        ('country', 'Country'),
        ('blues', 'Blues'),
        ('rnb', 'R&B'),
        ('reggae', 'Reggae'),
        ('folk', 'Folk'),
        ('metal', 'Metal'),
        ('soul', 'Soul'),
        ('funk', 'Funk'),
        ('disco', 'Disco'),
        ('kpop', 'K-Pop'),
        ('alternative', 'Alternative'),
        ('indie', 'Indie'),
        ('dubstep', 'Dubstep'),
        ('ambient', 'Ambient'),
        ('instrumental', 'Instrumental'),
        ('acoustic', 'Acoustic'),
        ('soundtrack', 'Soundtrack'),
    ]
    genre = models.CharField(max_length=255, choices=GENRE_CHOICES, verbose_name='Genre')
    users = models.ManyToManyField('UserProfile', related_name='songs', blank=True)
    
    def average_enjoyment(self):
        ratings = self.ratings.all()
        if ratings:
            return sum(r.enjoyment for r in ratings) / ratings.count()
        return 0
    

    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    liked_songs = models.ManyToManyField('Song', related_name='liked_by', blank=True)
    learned_songs = models.ManyToManyField('Song', related_name='learned_by', blank=True)
    bio = models.TextField(blank=True, verbose_name='Bio')

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

class Rating(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ratings')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='ratings')
    enjoyment = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    comments = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['user_profile', 'song']  # Each user can only rate a song once.
    
    def __str__(self):
        return f"{self.user_profile.user.username} - {self.song.name}"
