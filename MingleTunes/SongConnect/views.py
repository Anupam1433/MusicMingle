from django.shortcuts import render

from .models import artist, album, song

# def artist_list(request):
#     artists = artist.objects.all()
#     return render(request, 'songss/list.html', {'artists': artists})

# def artist_detail(request, artist_id):
#     artist_obj = artist.objects.get(pk=artist_id)
#     return render(request, 'songss/detail.html', {'artist': artist_obj})

def index(request):
    allSongs = song.objects.all().order_by('-updated_at')
    return render(request, template_name="try/index.html", context={"allSongs" : allSongs})
