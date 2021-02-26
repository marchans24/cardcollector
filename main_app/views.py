from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Card:
    def __init__(self, name, make, value, year):
        self.name = name
        self.make = make
        self.value = value
        self.year = year

cards = [
    Card('Patrick Mahomes', 'Panini', '23', '2018'),
    Card('Doug McDermott', 'Topps', '10', '2020')
]


# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    return render(request, 'cards/index.html', { 'cards': cards })