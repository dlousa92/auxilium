from django.db import models

# Create your models here.

class Event(models.Model):
  name= models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  ANIMALS = 'AN'
  ARTS = 'AR'
  YOUTH = 'YU'
  EDUCATION = 'ED'
  ELDERLY = 'EY'
  ENVIRONMENT ='EV'
  HOMELESS = 'HM'
  COMMUNITY = 'CY'
  TECH = 'TC'
  category_choices = (
    (ANIMALS, 'Animals'),
    (ARTS, 'Arts'),
    (YOUTH, 'Youth'),
    (EDUCATION, 'Education'),
    (ELDERLY, 'Elderly'),
    (ENVIRONMENT, 'Environment'),
    (HOMELESS, 'Homeless'),
    (COMMUNITY, 'Community'),
    (TECH, 'Tech')
  )
  date = models.DateField()
  description = models.TextField()
  volunteers_needed = models.IntegerField()

class Profile(models.Model):
  user = models.ForeignKey('auth.User', related_name='profile', on_delete=models.CASCADE)
  # email included in user auth
  # password included in user auth
  # name included in user auth
  number = models.CharField(max_length=13)
  INDIVIDUAL = 'IN'
  COMPANY ='CO'
  type_of_account = (
    (INDIVIDUAL, 'Individual'),
    (COMPANY, 'Company')
  )