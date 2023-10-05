from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class album(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    artist = models.ForeignKey(artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    cover = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name


class song(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    album = models.ForeignKey(album, on_delete=models.CASCADE)
    artist = models.ForeignKey(artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    length = models.FloatField()
    disc = models.IntegerField()
    lyrics = models.TextField()
    path = models.TextField()
    mtime = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('MingleTunes:artistDetails')
    

class interaction(models.Model):
    id = models.BigAutoField(primary_key=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(song, on_delete=models.CASCADE)
    liked = models.BooleanField()  
    play_count = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    # def __str__(self):
    #     return f"Interaction between {self.user} and {self.song}"

class playlist(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    rules = models.TextField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name


class PlaylistSong(models.Model):
    id = models.AutoField(primary_key=True)
    playlist = models.ForeignKey(playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(song, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"{self.playlist} - {self.song}"







