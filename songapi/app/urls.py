from django.urls import path
from app import views 
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("",views.index),
    path('songpost/', views.songpost),
    path('songs/', views.songs, name='songs'),
    path('songs/<int:id>', views.songpost, name='songpost'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
