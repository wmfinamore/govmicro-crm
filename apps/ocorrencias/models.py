from django.db import models
from apps.core.models import Auditoria
from django.contrib.auth import get_user_model
from apps.assuntos.models import Assunto
from apps.enderecos.models import Endereco
from apps.unidades.models import Unidade
import uuid
from datetime import date


User = get_user_model()


class Ocorrencia(Auditoria):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero = models.PositiveBigIntegerField(null=True, blank=True)
    solicitante = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, limit_choices_to={'is_staff': False}, )
    ano = models.PositiveIntegerField(default=date.today().strftime("%Y"), editable=False)
    assunto = models.ForeignKey(Assunto, on_delete=models.PROTECT, limit_choices_to={'folha': True}, )
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT, verbose_name='Endereço')
    anonimo = models.BooleanField(default=False, verbose_name='Anônimo?')
    descricao_ocorrencia = models.TextField(null=True, blank=True, verbose_name='Descrição da Ocorrência')
    unidade_atual = models.ForeignKey(Unidade, blank=True, null=True, on_delete=models.PROTECT, editable=False)

    def save(self, *args, **kwargs):
        # Regra para geração de numeração
        if self.numero is not None:
            pass
        else:
            numero = Ocorrencia.objects.filter(ano=date.today().strftime("%Y")).order_by('-numero').first()
            if numero:
                self.numero = int(numero.numero) + 1
            else:
                self.numero = 1

        # Regra para atribuição de número a ocorrência
        if self.unidade_atual is None:
            assunto = Assunto.objects.get(id=self.assunto.id)
            self.unidade_atual = assunto.unidade
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.solicitante) + ' - ' + str(self.assunto) + ' - ' + str(self.endereco)
