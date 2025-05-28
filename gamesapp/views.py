from django.shortcuts import render

from django.db import models

from .models import Game
# Create your views here.

def home(request):
    games = Game.objects.all()
    return render(request,"index.html", {"games":games})


def game(request, id):
    game1 = Game.objects.get(id=id)
    return render(request, "game.html", {"game": game1})

def search(request):
    query = request.GET.get('search')
    games = Game.objects.all()

    if query:
        games = games.filter(
            models.Q(title__icontains=query) |
            models.Q(genre__icontains=query)
        )

    return render(request, 'search.html', {'games': games, 'query': query})