from rest_framework import serializers

from .models import Album, Musician, Song


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ('name',) 


class AlbumSerializer(serializers.ModelSerializer):
    musician = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Album
        fields = ('musician', 'year')


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('name', 'number')
