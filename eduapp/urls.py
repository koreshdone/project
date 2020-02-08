from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ehome/',views.ehome),
    path('btech/',views.btech),
    path('sem/',views.sem),
    path('sem2/',views.sem2),
    path('other/',views.other),
]