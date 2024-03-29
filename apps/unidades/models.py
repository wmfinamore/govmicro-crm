from django.contrib.auth import get_user_model
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from simple_history.models import HistoricalRecords

User = get_user_model()


class Unidade(MPTTModel):
    nome = models.CharField(max_length=100, verbose_name='Nome da Unidade')
    sigla = models.CharField(max_length=10, null=True, blank=True, verbose_name='Sigla')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    ativo = models.BooleanField(default=True)
    funcionarios = models.ManyToManyField(User, blank=True, limit_choices_to={'is_staff': True}
                                          , related_name='unidades'
                                         )
    history = HistoricalRecords(excluded_fields=['lft', 'rght', 'tree_id', 'level'])

    def __str__(self):
        return str(self.sigla) + ' - ' + self.nome

