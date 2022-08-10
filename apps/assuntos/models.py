from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from apps.core.models import Auditoria


class Assunto(MPTTModel, Auditoria):
    nome = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.nome
