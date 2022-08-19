from .models import Endereco
from django.test import TestCase


class EnderecoTests(TestCase):
    """
    Teste de criação de Endereco
    """
    def test_create_endereco(self):
        endereco = Endereco.objects.create(
            endereco='Avenida Engenheiro Carlos Reinaldo Mendes',
            bairro='Alto da Boa Vista',
            cep='18013280',
        )
        self.assertEqual(endereco.endereco, 'Avenida Engenheiro Carlos Reinaldo Mendes')
        self.assertEqual(endereco.bairro, 'Alto da Boa Vista')
        self.assertEqual(endereco.cep, '18013280')
        self.assertEqual(endereco.cidade, 'Sorocaba')  # test default value
        self.assertEqual(endereco.estado, 'SP')  # test default value
