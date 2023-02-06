from rest_framework import serializers

from .models import Album, Artist, Song


class TrackSerializer(serializers.ModelSerializer[Song]):
    class Meta:
        model = Song
        fields = ("name", "number")


class AlbumViewSetSerializer(serializers.ModelSerializer[Album]):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ("published", "tracks")


class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumViewSetSerializer(many=True)

    class Meta:
        model = Artist
        fields = ("name", "albums")
