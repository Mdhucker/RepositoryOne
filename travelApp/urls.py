from django.contrib import admin
from django.urls import include,path
from . import views

from django.urls import path


urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('services/', views.services, name='services'),
    path('packages/', views.packages, name='packages'),
    path('destination/', views.destination, name='destination'),
    path('booking/', views.booking, name='booking'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('errorpage/', views.errorpage, name='errorpage'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),

    path('gallary/', views.gallary, name='gallary'),


    path('redirect/<str:platform>/', views.social_media_redirect, name='social_media_redirect'),

  
]


