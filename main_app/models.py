from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=250)
    make = models.CharField(max_length=250)
    value = models.CharField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return self.name