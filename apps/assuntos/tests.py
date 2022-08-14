from .models import Assunto
from django.test import TestCase


class AssuntoTests(TestCase):
    """
    Teste de criação de assunto
    """
    def test_create_assunto(self):
        assunto = Assunto.objects.create(
            nome='Assunto Primário',
        )
        self.assertEqual(assunto.nome, 'Assunto Primário')
        self.assertEqual(assunto.level, 0)

        assunto_secundario = Assunto.objects.create(
            nome='Assunto Secundário',
            parent=assunto
        )
        self.assertEqual(assunto_secundario.nome, 'Assunto Secundário')
        self.assertEqual(assunto_secundario.level, 1)
