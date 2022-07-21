from django.db import models

# Create your models here.

class CaffeineUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_email = models.EmailField('User Email Address')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Venue(models.Model):
    venue_name = models.CharField('Venue Name', max_length=120)
    venue_address = models.CharField(max_length=120)
    phone = models.CharField('Contact Phone No.',max_length=120)
    web = models.URLField('Website Address')
    email = models.EmailField('Email Address')

    def __str__(self):
        return self.venue_name

class Event(models.Model):
    event_name = models.CharField('Event Name', max_length=50)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField(max_length=120)
    event_desc = models.TextField(blank=True)
    attendees = models.ManyToManyField(CaffeineUser, blank=True)

    def __str__(self):
        return self.event_name