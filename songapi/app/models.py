from django.db import models

# Create your models here.

class Song(models.Model):
    song_id = models.AutoField(primary_key= True)
    songname = models.CharField(max_length = 150, null=False, blank = False)
    songimage = models.ImageField(upload_to = 'image')
    songaudio = models.FileField(upload_to= 'audio')
    singer = models.CharField(max_length= 2000)
    songmoviename = models.CharField(max_length = 150, default = "None")
    duration= models.IntegerField(null=False, blank = False)
    uploaded= models.DateTimeField(auto_now_add = True)
    