from django import forms
from .models import Event, Profile

class EventForm(forms.ModelForm):

  class Meta:
    model = Event
    fields = ('name', 'location', 'date', 'description', 'volunteers_needed')

class ProfileForm(forms.ModelForm):

  class Meta:
    model = Profile
    fields = ('number',)