from django.db import models
from .resourses import STATUS


class Users(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=9)
    surname = models.CharField(max_length=25)
    name = models.CharField(max_length=15)
    patronymic = models.CharField(max_length=15)


class Pereval(models.Model):
    beauty_title = models.CharField(max_length=10, default='пер.')
    title = models.CharField(max_length=25)
    other_titles = models.CharField(max_length=25)
    connect = models.CharField(max_length=25, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    level_winter = models.CharField(max_length=2, blank=True)
    level_summer = models.CharField(max_length=2, blank=True)
    level_autumn = models.CharField(max_length=2, blank=True)
    level_spring = models.CharField(max_length=2, blank=True)
    status = models.CharField(max_length=2, choices=STATUS)


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Image(models.Model):
    name = models.CharField(max_length=50)
    foto = models.ImageField


class PerevalImage(models.Model):
    foto = models.ForeignKey(Image, on_delete=models.CASCADE)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE)
