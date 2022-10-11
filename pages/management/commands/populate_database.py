from django.core.management.base import BaseCommand
from django.db import connection
from pages.models import DoacaoRecebida, UnidadeOrganizacao, Produto, DoacaoAgendada
import random
import datetime
from faker import Faker


class Command(BaseCommand):
    def add_arguments(self, parser):
        ...
    
    def get_produtos_cadastrados(self):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT * FROM pages_produto;
                """
            )
            rows = cursor.fetchall()
        
        return rows

    def generate_fake_doacoes_recebidas(self, produtos_cadastrados_rows):
        faker = Faker('pt_BR')
        recebido = DoacaoRecebida(
            unidadeOrganizacao=UnidadeOrganizacao.objects.get(nome="Igreja"), ## foreign
            # doador=faker.name(), ## foreign
            produto=random.choice(produtos_cadastrados_rows), ## foreign
            status=random.choice(['EST', 'ENT', 'PER']),
            quantidade=int(random.random()*10),
            dataRecebimento=datetime.datetime(2022, 9, 30),
            dataBaixa=datetime.datetime(2022, 9, 30),
            doacaoAgendada=None, ## foreign
            dataValidade=datetime.datetime(2022, 11, 15),
            doacaoViaWeb=random.choice([True, False]),
            saldoDeEntrega=True
            )
        return recebido

    def generate_fake_produtos_agendados(self):
        pass


    def handle(self, *args, **kwargs):
        produtos_cadastrados_rows = list(Produto.objects.all())
        data = [self.generate_fake_doacoes_recebidas(produtos_cadastrados_rows) for i in range(2)]
        DoacaoRecebida.objects.bulk_create(data, ignore_conflicts=True)

