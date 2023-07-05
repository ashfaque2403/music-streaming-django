from app.helpers import get_audio_length
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# from app.models import Comment


# Create your models here.
class Song(models.Model):
    song_name=models.CharField(max_length=200)
    artist_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media/',blank=True,null=True)
    audio_file=models.FileField(upload_to='media/',blank=True,null=True)
    album=models.ForeignKey('Playlist',on_delete=models.SET_NULL,null=True,blank=True)
    # audio_link=models.FileField(max_length=200,blank=True,null=True)
    duration=models.DecimalField(blank=True,max_digits=20,decimal_places=2)
    favourites=models.ManyToManyField(User,related_name='favourite+',default=None,blank=True)

    

    def __str__(self):
        return self.song_name

    # def get_absolute_url(self):
    #     return reverse('/', kwargs={'pk': self.pk})

    def save(self):
        if not self.duration:
            # logic for getting audio length
            
            audio_length=get_audio_length(self.audio_file)
            self.duration=audio_length
        return super().save()

class Playlist(models.Model):
    playlist_title=models.CharField(max_length=50)
    play_image=models.ImageField(upload_to='sng/',blank=True,null=True)
    playlist_artist=models.CharField(max_length=50)
    
    def __str__(self):
        return self.playlist_title

class Artist(models.Model):
    artist_name=models.CharField(max_length=50)
    artist_image=models.ImageField(upload_to='Artist/',blank=True,null=True)

    def __str__(self):
        return self.artist_name


class UserProfile(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)
    pro_image=models.ImageField(upload_to='pro_pics/',null=True,blank=True)

from django.db import models

class Comment(models.Model):
    post = models.ForeignKey('app.Playlist', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
