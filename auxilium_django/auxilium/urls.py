from django.urls import path
from . import views

urlpatterns = [
  path('', views.event_list, name='event_list'),
  path('event/<int:pk>', views.event_detail, name='event_detail'),
  path('event/new', views.event_create, name='event_create'),
  path('event/<int:pk>/edit', views.event_edit, name='event_edit'),
  path('event/<int:pk>/delete', views.event_delete, name='event_delete'),

  path('profile/<int:pk>', views.profile_detail, name='profile_detail'),
  path('profile/new', views.profile_create, name='profile_create')
]