from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Event, Profile
from .forms import EventForm, ProfileForm

def event_list(request):
  events = Event.objects.all()
  return render(request, 'auxilium/event_list.html', {'events': events})
def event_detail(request, pk):
  event = Event.objects.get(id=pk)
  return render(request, 'auxilium/event_detail.html', {'event': event})
def event_create(request):
  if request.method == 'POST':
    form = EventForm(request.POST)
    if form.is_valid():
      event = form.save()
      return redirect('event_detail', pk=event.pk)
  else:
    form = EventForm()
  return render(request, 'auxilium/event_form.html', {'form': form})
def event_edit(request, pk):
  event = Event.objects.get(id=pk)
  if request.method == 'POST':
    form = EventForm(request.POST, instance=event)
    if form.is_valid():
      event = form.save()
      return redirect('event_detail', pk=event.pk)
  else: form = EventForm(instance=event)
  return render(request, 'auxilium/event_form.html', {'form': form})
def event_delete(request, pk):
  Event.objects.get(id=pk).delete()
  return redirect('event_list')

def sign_up(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('profile_create')
  else:
    form = UserCreationForm()
  return render(request, 'registration/signup.html', {'form': form})

def profile_detail(request, pk):
  profile = Profile.objects.get(id=pk)
  return render(request, 'auxilium/profile_detail.html', {'profile': profile})
def profile_create(request):
  if request.method == 'POST':
    form = ProfileForm(request.POST)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = request.user
      return redirect('profile_detail', pk=profile.pk)
  else:
    form = ProfileForm()
  return render(request, 'auxilium/profile_form.html', {'form': form})