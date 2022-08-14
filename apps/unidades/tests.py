from .models import Unidade
from django.test import TestCase


class UnidadeTests(TestCase):
    """
    Teste de criação de unidade
    """
    def test_create_unidade(self):
        unidade = Unidade.objects.create(
            nome='Secretaria',
            sigla='SE',
            ativo=True,
        )
        self.assertEqual(unidade.nome, 'Secretaria')
        self.assertEqual(unidade.sigla, 'SE')
        self.assertTrue(unidade.ativo)
        self.assertEqual(unidade.level, 0)

        unidade_secundaria = Unidade.objects.create(
            nome='Divisão',
            sigla='DI',
            ativo=True,
            parent=unidade
        )
        self.assertEqual(unidade_secundaria.nome, 'Divisão')
        self.assertEqual(unidade_secundaria.sigla, 'DI')
        self.assertTrue(unidade_secundaria.ativo)
        self.assertEqual(unidade_secundaria.level, 1)
