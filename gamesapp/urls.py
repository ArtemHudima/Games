from django.urls import path
from .views import home, game
urlpatterns = [
    path('', home, name="home"),
    path('game/<int:id>', game, name="game"),

]
