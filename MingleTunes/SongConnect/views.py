from django.shortcuts import render

from .models import artist, album, song

def artist_list(request):
    artists = artist.objects.all()
    return render(request, 'songss/artist_list.html', {'artists': artists})

def artist_detail(request, artist_id):
    artist_obj = artist.objects.get(pk=artist_id)
    return render(request, 'songss/artist_detail.html', {'artist': artist_obj})
