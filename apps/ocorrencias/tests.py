from django.test import TestCase
from .models import Ocorrencia
from apps.enderecos.models import Endereco
from apps.assuntos.models import Assunto
from django.contrib.auth import get_user_model


class OcorrenciaTests(TestCase):
    def setUp(self):
        pass

    def test_ocorrencia_listing(self):
        pass
