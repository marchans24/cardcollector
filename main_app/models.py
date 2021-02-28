from django.db import models
from django.urls import reverse

LOCATION = (
    ('O', 'Online'),
    ('S', 'Store'),
    ('U', 'Unknown'),
)

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

class Acquired(models.Model):
    date = models.DateField('acquired date')
    location = models.CharField(max_length=1, choices=LOCATION, default=LOCATION[0][0])

    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_location_display()} at {self.date}"

    class Meta:
        ordering = ['-date']