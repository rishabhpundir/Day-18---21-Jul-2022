from django.urls import path
from CafClubApp import views

urlpatterns = [
    path('', views.home, name='home_link'),
    path('events', views.all_events, name='events_link'),
]
