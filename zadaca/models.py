from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Artist(models.Model):
    ART_STYLES = [
        ('imp', 'impressionism'),
        ('pop', 'pop art'),
        ('graffiti', 'graffiti')
    ]
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    style = models.CharField(max_length=30, choices=ART_STYLES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.surname

class Artwork(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='zadaca')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    exhibition = models.ForeignKey('Exhibition', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Exhibition(models.Model):
    title = models.CharField(max_length=100)
    date_from = models.DateField()
    date_to = models.DateField(blank=True, null=True)
    description = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title + ' ' + str(self.date_from) + '-' + str(self.date_to)