from django.test import TestCase
from .models import Ocorrencia
from apps.enderecos.models import Endereco
from apps.unidades.models import Unidade
from apps.assuntos.models import Assunto
from django.contrib.auth import get_user_model

User = get_user_model()


class OcorrenciaTests(TestCase):
    def setUp(self):
        self.solicitante = User.objects.create(
            username='testUser',
            cpf='465.904.190-51',
            email='email@email.com',
            password='A12345678a'
        )

        self.unidade = Unidade.objects.create(
            nome='Secretaria',
            sigla='SE',
        )

        self.assunto = Assunto.objects.create(
            nome='Teste Unitário',
            unidade=self.unidade
        )

        self.endereco = Endereco.objects.create(
            endereco='Rua da Validação',
            bairro='Centro',
            cidade='Soro City',
            estado='SP',
            cep='18015000'
        )

        self.ocorrencia = Ocorrencia.objects.create(
            solicitante=self.solicitante,
            assunto=self.assunto,
            endereco=self.endereco,
            descricao_ocorrencia='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sit amet dictum'
                                 ' augue. Nulla eget turpis pretium, luctus est nec, pellentesque enim. Vestibulum '
                                 'ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; '
                                 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames'
                                 ' ac turpis egestas. Phasellus quis enim a felis cursus sagittis quis nec lectus.'
                                 ' Nam fringilla mollis lectus ut egestas. Phasellus placerat egestas sem. Donec vel'
                                 ' nisi sem. Suspendisse ex sem, efficitur sed hendrerit nec, pellentesque vitae magna.'
        )

    def test_ocorrencia_listing(self):
        self.assertEqual(f'{self.ocorrencia.solicitante.username}', 'testUser')
        self.assertEqual(f'{self.ocorrencia.assunto.nome}', 'Teste Unitário')
        self.assertEqual(f'{self.ocorrencia.endereco.cep}', '18015000')
        self.assertEqual(f'{self.ocorrencia.unidade_atual.nome}', 'Secretaria')
        self.assertEqual(f'{self.ocorrencia.descricao_ocorrencia}',
                         'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sit amet dictum'
                         ' augue. Nulla eget turpis pretium, luctus est nec, pellentesque enim. Vestibulum '
                         'ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; '
                         'Pellentesque habitant morbi tristique senectus et netus et malesuada fames'
                         ' ac turpis egestas. Phasellus quis enim a felis cursus sagittis quis nec lectus.'
                         ' Nam fringilla mollis lectus ut egestas. Phasellus placerat egestas sem. Donec vel'
                         ' nisi sem. Suspendisse ex sem, efficitur sed hendrerit nec, pellentesque vitae magna.'
                         )
