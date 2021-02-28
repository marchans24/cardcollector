from django.db import models
from django.urls import reverse

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=250)
    make = models.CharField(max_length=250)
    value = models.CharField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cards_detail', kwargs={'card_id': self.id})