from django.shortcuts import render

# Create your views here.

from .models import Treasure


def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures': treasures})


def detail(request, slug):
    treasure = Treasure.objects.get(slug=slug)

    return render(request, 'detail.html', {'treasure': treasure})

