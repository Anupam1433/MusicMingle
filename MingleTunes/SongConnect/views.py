from django.shortcuts import render

from .models import artist, album, song

def index(request):
    allSongs = song.objects.all().order_by('-updated_at')
    return render(request, template_name="mingletunes/index.html", context={"allSongs" : allSongs})
