from django.contrib import admin
from CafClubApp.models import Venue, CaffeineUser, Event

# Register your models here.
admin.site.register(CaffeineUser)
admin.site.register(Venue)
admin.site.register(Event)