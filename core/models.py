from django.db import models


class Jogo(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Campeonato')
    local = models.CharField(max_length=100, verbose_name='Local')
    data = models.DateTimeField(verbose_name='Data e hora do jogo')
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
        ordering = ['nome']


class Campeonato(models.Model):
    jogo = models.ForeignKey(Jogo, related_name='jogo', on_delete=models.CASCADE, verbose_name='Jogo')
    time = models.CharField(max_length=10, verbose_name='Time')
    gol = models.PositiveIntegerField(verbose_name='Gols')

    def __str__(self):
        return f'{self.time}'
