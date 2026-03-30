from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'base'

urlpatterns = [
     path('', HomePageView.as_view(), name='home'),
     path('about-us/', about_us, name='about_us'),
     path('market/', market, name='market'),
     path('sale/', sale, name='sale'),
     path('help/', help_page, name='help'),    
]
