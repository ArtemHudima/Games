from django.urls import path
from .views import home, game, search
urlpatterns = [
    path('', home, name="home"),
    path('game/<int:id>', game, name="game"),
    path('search/', search, name="search"),

]
