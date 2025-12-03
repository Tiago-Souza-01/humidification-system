from django.db import models


class Configuracao(models.Model):
    """Global configuration (singleton-like) to hold the desired setpoint."""
    setpoint = models.FloatField(default=50.0)

    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configurações'

    def __str__(self):
        return f"Setpoint: {self.setpoint}"


class Telemetria(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    umidade = models.FloatField()
    setpoint = models.FloatField()
    sistema_ativo = models.BooleanField(default=False)
    atuando = models.BooleanField(default=False)
    nivel_agua_baixo = models.BooleanField(default=False)
    violacao_geral = models.BooleanField(default=False)
    alarme = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.timestamp} - {self.umidade}%"
