from django.contrib import admin
from .models import User
from .models import Song

admin.site.register(User )
admin.site.register(Song)