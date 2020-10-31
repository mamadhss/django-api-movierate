from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)
    

class Rating(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='rates')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) 
    stars = models.IntegerField(validators=[MinValueValidator(1),
    MaxValueValidator(5)])

    