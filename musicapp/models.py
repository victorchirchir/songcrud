from datetime import datetime
from email.policy import default
from enum import unique
from pickle import TRUE
from tkinter import CASCADE
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

# Create your models here.
class Artiste(models.Model):
    first_name=models.CharField(max_length=400)
    last_name=models.CharField(max_length=400)
    age=models.IntegerField(default=0)

    def __str__(self):
        return self.first_name 
        
class Song(models.Model):
    title=models.CharField(max_length=400)
    date_released=models.DateField(default=datetime.today)
    likes=models.IntegerField(default=0)
    artiste_ColumnId=models.IntegerField(default=0)
    Artiste=models.ForeignKey(Artiste,on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    

class Lyric(models.Model):
    content=models.CharField(max_length=40000000000)
    song_Columnid=models.IntegerField()
    Song=models.ForeignKey(Song,on_delete=models.CASCADE)
