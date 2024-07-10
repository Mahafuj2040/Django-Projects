from django.db import models
from musician.models import Musician



class Albumb(models.Model):
    
    RATING_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albumbs')
    albumb_name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.CharField(max_length=1,choices=RATING_CHOICES)

    def __str__(self) -> str:
        return self.albumb_name
