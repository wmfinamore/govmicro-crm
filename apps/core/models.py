from django.db import models
from simple_history.models import HistoricalRecords


class Auditoria(models.Model):
    data_inclusao = models.DateField(auto_now_add=True, editable=False, verbose_name="Data de Inclusão")
    hora_inclusao = models.TimeField(auto_now_add=True, editable=False, verbose_name="Hora de Inclusão")
    data_alteracao = models.DateTimeField(auto_now=True, editable=False, verbose_name="Data de Alteração")
    hora_alteracao = models.TimeField(auto_now=True, editable=False, verbose_name="Hora de Alteração")
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
