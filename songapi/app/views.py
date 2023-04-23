from django.shortcuts import render, redirect
from .models import Song


def index(request):
    song = Song.objects.all()
    return render(request, 'index.html', {'song': song})


def songs(request):
    song = Song.objects.all()
    return render(request, 'songs.html', {'song': song})

def songpost(request, id):
    song = Song.objects.filter(song_id = id).first()
    return render(request, 'songpost.html', {'song': song})
