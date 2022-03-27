from django.contrib import admin
from core.models import Jogo, Campeonato


class CampeonatoInline(admin.TabularInline):
    model = Campeonato
    extra = 1
    min_num = 2
    max_num = 2


class TimeAdmin(admin.ModelAdmin):
    inlines = [
        CampeonatoInline
    ]


admin.site.register(Jogo, TimeAdmin)
