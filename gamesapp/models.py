from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to="media")
    date = models.DateField()
    genre = models.CharField(max_length=150)
    age = models.IntegerField()
