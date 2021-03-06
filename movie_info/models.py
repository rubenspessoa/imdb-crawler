from django.db import models
from numpy import unique

class Director(models.Model):
    director = models.CharField(max_length=500, unique=True)
    
class Language(models.Model):
    language = models.CharField(max_length=500, unique=True)
    
class Genre(models.Model):
    genre = models.CharField(max_length=500, unique=True)

class Country(models.Model):
    country = models.CharField(max_length=500, unique=True)
    
class Movie(models.Model):
    id_movie = models.CharField(max_length=200, unique=True)
    rating = models.CharField(max_length=200)
    votes = models.CharField(max_length=200)
    year = models.CharField(max_length=10)
    
    genre = models.ManyToManyField(Genre)
    country = models.ManyToManyField(Country)
    language = models.ManyToManyField(Language)
    directors = models.ManyToManyField(Director)
    
    def __init__(self, id_movie, rating, votes, year):
        super(Movie, self).__init__()
        self.id_movie = id_movie
        self.rating = rating
        self.votes = votes
        self.year = year
