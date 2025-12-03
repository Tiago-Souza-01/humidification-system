from django.contrib import admin
from .models import Telemetria, Configuracao


@admin.register(Telemetria)
class TelemetriaAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'umidade', 'setpoint', 'sistema_ativo', 'atuando', 'nivel_agua_baixo', 'violacao_geral', 'alarme')
    list_filter = ('sistema_ativo', 'atuando', 'nivel_agua_baixo', 'violacao_geral', 'alarme')
    readonly_fields = ('timestamp',)


@admin.register(Configuracao)
class ConfiguracaoAdmin(admin.ModelAdmin):
    list_display = ('setpoint',)
