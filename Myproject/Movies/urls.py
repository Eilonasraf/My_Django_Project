from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [path('Movies/', views.Movies, name='Movies'),
               path('movie_details/<movie_id>', views.movie_details, name='movie_details')]
