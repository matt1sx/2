from django.shortcuts import render, get_list_or_404
from .models import Campeonato, Jogo


def home(request):
    campeonato = Campeonato.objects.filter(jogo__finalizado=True)
    return render(request, 'pages/index.html', {'campeonato': campeonato})


def ranking(request):
    jogo = Campeonato.objects.filter(jogo__finalizado=True).order_by('-gol')
    return render(request, 'pages/ranking.html', {'jogo': jogo})
