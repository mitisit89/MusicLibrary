from django.db import models


class Album(models.Model):
    published = models.DateField()


class Artist(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Album, related_name="albums", on_delete=models.CASCADE)


class Song(models.Model):

    album = models.ForeignKey(Album, related_name="tracks", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    number = models.PositiveSmallIntegerField()
