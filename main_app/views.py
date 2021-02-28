from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Card
from .forms import AcquiredForm



# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', { 'cards': cards })

def cards_detail(request, card_id):
  card = Card.objects.get(id=card_id)
  acquired_form = AcquiredForm()
  return render(request, 'cards/detail.html', { 'card': card, 'acquired_form': acquired_form })

def add_acquired(request, card_id):
  form = AcquiredForm(request.POST)
  if form.is_valid():
    new_acquired = form.save(commit=False)
    new_acquired.card_id = card_id
    new_acquired.save()
  return redirect('cards_detail', card_id=card_id)

class CardCreate(CreateView):
    model = Card
    fields = '__all__'
    
class CardUpdate(UpdateView):
    model = Card
    fields = ['make', 'value', 'year']

class CardDelete(DeleteView):
    model = Card
    success_url = '/cards/'