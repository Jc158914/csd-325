# Juan Cardenas
# 11/22/2026
# Module 11.2 Assignment
# Purpose: Displays a personalized greeting using Django.

from django.http import HttpResponse


def home(request):
    return HttpResponse("Cardenas says Hello!")