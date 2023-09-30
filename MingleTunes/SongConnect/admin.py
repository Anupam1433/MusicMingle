from django.contrib import admin

# Register your models here.

from .models import artist, album, song, interaction, playlist, PlaylistSong

# Register your models here
admin.site.register(artist)
admin.site.register(album)
admin.site.register(song)
admin.site.register(interaction)
admin.site.register(playlist)
admin.site.register(PlaylistSong)
