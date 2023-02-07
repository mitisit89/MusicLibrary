from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)


class Album(models.Model):
    published = models.DateField()
    artist = models.ForeignKey(Artist, related_name="artists", on_delete=models.CASCADE)


class Song(models.Model):

    album = models.ForeignKey(Album, related_name="tracks", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    number = models.PositiveSmallIntegerField()
