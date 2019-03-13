# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Movie(models.Model):
    owner = models.ForeignKey('auth.User', related_name='movies')
    name = models.CharField(max_length=100)
    popularity = models.DecimalField(decimal_places=1, max_digits=3,
                                     validators=[MinValueValidator,
                                                 MaxValueValidator])
    director = models.CharField(max_length=100)
    imdb_score = models.DecimalField(decimal_places=1, max_digits=3,
                                     validators=[MinValueValidator,
                                                 MaxValueValidator])
    genre = models.ManyToManyField(Genre)


    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name