from .models import Song
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from .models import Song, Rating

# Define an inline admin descriptor for the UserProfile model
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

# Re-register UserAdmin with the updated settings
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(UserProfile )
admin.site.register(Song)
admin.site.register(Rating)