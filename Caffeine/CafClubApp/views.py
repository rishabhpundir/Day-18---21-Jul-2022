from wsgiref.util import request_uri
from django.shortcuts import render
from .models import Event

# Create your views here.
def home(request):
    return render(request, 'events/home.html')

def all_events(request):
    events = Event.objects.all()
    return render(request, 'events/events_list.html', context={'events':events})