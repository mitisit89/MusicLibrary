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


class ArtistSerializer(serializers.ModelSerializer[Artist]):
    artists = AlbumViewSetSerializer(
        many=True,
    )

    class Meta:
        model = Artist
        fields = ("name", "artists")

    def create(self, validated_data) -> "Artist":
        artist = Artist.objects.create(name=validated_data.pop("name"))

        for album in validated_data.values():
            for track in album:

                album = Album.objects.create(
                    artist=artist, published=track.pop("published")
                )
                print(track)
                for songs in track.values():
                    for song in songs:
                        Song.objects.create(
                            name=song["name"], album=album, number=song["number"]
                        )
        artist.save()
        return artist
