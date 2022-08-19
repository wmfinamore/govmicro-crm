from django.db import models
from apps.core.models import Auditoria
from config.settings import CIDADE, ESTADO


class Endereco(Auditoria):
    endereco = models.CharField(max_length=250, verbose_name='Endereço')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')
    cidade = models.CharField(max_length=100, verbose_name='Cidade', default=CIDADE)
    estado = models.CharField(max_length=100, verbose_name='Estado', default=ESTADO)
    cep = models.CharField(max_length=8, verbose_name='CEP')

    def __str__(self):
        return self.endereco + ', ' + self.bairro + ', ' + self.cidade + ', ' + self.estado + ', ' + self.cep
