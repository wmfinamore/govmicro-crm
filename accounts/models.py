from django.contrib.auth.models import AbstractUser
from django.db import models
from django_cpf_cnpj.fields import CPFField
import uuid
from apps.core.models import Auditoria


# Atributos customizados devem ser adicionados aqui
class CustomUser(AbstractUser, Auditoria):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpf = CPFField(masked=True, null=True, blank=True, verbose_name="CPF")
    matricula = models.PositiveBigIntegerField(null=True, blank=True, verbose_name="Matrícula")

