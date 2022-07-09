from django.contrib.auth.models import AbstractUser
from django.db import models
from django_cpf_cnpj.fields import CPFField


# Atributos customizados devem ser adicionados aqui
class CustomUser(AbstractUser):
    cpf = CPFField(masked=True, null=True, blank=True, verbose_name="CPF")
    matricula = models.PositiveBigIntegerField(max_length=6, null=True, blank=True, verbose_name="Matrícula")

