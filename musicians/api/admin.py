from django.contrib import admin

from .models import Album, Musician, Song

admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Song)
