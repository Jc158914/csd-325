# Juan Cardenas
# 11/22/2026
# Module 11.2 Assignment
# Purpose: Defines the URL route for the homepage.

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
]