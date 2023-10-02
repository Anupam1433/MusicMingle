from django.shortcuts import render

# from .models import artist, album, song, PlaylistSong, playlist, interaction

# def index(request):
#     allSongs = song.objects.all().order_by('-updated_at')
#     return render(request, template_name="mingletunes/index.html", context={"allSongs" : allSongs})


# from django.shortcuts import render
from .models import PlaylistSong, playlist, interaction, song, album, artist

def index(request):
    # Retrieve objects from different models
    playlist_songs = PlaylistSong.objects.all()
    playlists = playlist.objects.all().order_by('-created_at')
    interactions = interaction.objects.all().order_by('-created_at')
    songs = song.objects.all().order_by('-updated_at')
    

    # Combine the objects into a single list
    allSongs = list(playlist_songs) + list(playlists) + list(interactions) + list(songs)

    # Sort the combined list by a common field like 'created_at' or 'updated_at'
    # all_content.sort(key=lambda x: x.created_at if hasattr(x, 'created_at') else x.updated_at, reverse=True)

    return render(request, template_name="mingletunes/index.html", context={"allSongs": allSongs})


