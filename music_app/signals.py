from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
from django.apps import apps


# signals.py

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile = apps.get_model('music_app', 'UserProfile')
    # It's safe to call save on UserProfile instance since it's created above if not exist
    instance.userprofile.save()