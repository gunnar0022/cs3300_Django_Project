# music_app/apps.py
from django.apps import AppConfig

class MusicAppConfig(AppConfig):
    name = 'music_app'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        from . import signals  # Local import to avoid circular dependency
