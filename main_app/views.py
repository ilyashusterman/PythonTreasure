from django.shortcuts import render

# Create your views here.

from .models import Treasure


def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures': treasures})
