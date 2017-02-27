from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
# Create your views here.
from .forms import TreasureForm
from .models import Treasure


def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures': treasures})


def detail(request, slug):
    treasure = Treasure.objects.get(slug=slug)
    return render(request, 'detail.html', {'treasure': treasure})


def edit(request, slug):
    treasure = Treasure.objects.get(slug=slug)
    if (request.method == 'POST'):
        # Proccess the form
        form = TreasureForm(data=request.POST, instance=treasure)
        if form.is_valid:
            form.save(commit=True)

        return redirect(reverse('detail', args=[slug,]))
        pass
    else:
        treasure_dict = model_to_dict(treasure)
        form = TreasureForm(treasure_dict)
        return render(request, 'edit.html', {'form': form})
