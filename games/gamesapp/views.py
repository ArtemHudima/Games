from django.shortcuts import render
from .models import Game
# Create your views here.

def home(request):
    games = Game.objects.all()
    return render(request,"index.html", {"games":games})

def game(request, id):
    game1 = Game.objects.get(id=id)
    return render(request, "game.html", {"game": game1})