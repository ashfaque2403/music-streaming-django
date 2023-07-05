from django.contrib import admin
from .models import Song,Playlist,Artist,UserProfile,Comment
# Register your models here.
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(Artist)
admin.site.register(UserProfile)
admin.site.register(Comment)
