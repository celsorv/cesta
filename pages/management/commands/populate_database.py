from django.core.management.base import BaseCommand
from django.db import connection
from pages.models import DoacaoRecebida, UnidadeOrganizacao, Produto, DoacaoAgendada
from users.models import User
import random
import datetime
from faker import Faker


class Command(BaseCommand):
    def add_arguments(self, parser):
        ...

    def generate_fake_doacoes_recebidas(self, produtos, organizacao, users_agendados_pendentes):
        '''
        Caso seja agendamento PEN (pendente), ira atualizar para REC (recebido)
        caso contrario, ira usar None (nao identificado) como doador
        '''

        agendado = random.choice(users_agendados_pendentes)
        if agendado.status == 'PEN':
            upd_agendada = DoacaoAgendada.objects.get(id=agendado.id)
            upd_agendada.status = 'REC'
            upd_agendada.save()

            doador = User.objects.get(id=agendado.doador.id)

        else:
            agendado = doador = None


        recebido = DoacaoRecebida(
            unidadeOrganizacao=organizacao, ## foreign
            doador=doador, ## foreign
            produto=random.choice(produtos), ## foreign
            status='EST',
            quantidade=random.randint(1, 10),
            dataRecebimento=datetime.datetime.today(),
            dataBaixa=datetime.datetime.today(),
            doacaoAgendada=agendado, ## foreign
            dataValidade=datetime.datetime(2022, 11, 15),
            doacaoViaWeb=random.choice([True, False]),
            saldoDeEntrega=True
            )
        return recebido

    def generate_fake_doacoes_agendadas(self, produtos, organizacao, users):
        agendada = DoacaoAgendada(
            unidadeOrganizacao=organizacao, ## foreign
            doador=random.choice(users), ## foreign
            produto=random.choice(produtos), ## foreign
            dataAgendamento=datetime.datetime.today(),
            status='PEN'
        )
        return agendada

    def generate_fake_users(self):
        faker = Faker('pt_BR')
        name = faker.name()
        user = User(
            is_superuser=False,
            ## many to many error ? not needed for testing ?
            ## groups=[101],
            ## user_permissions=[],
            password='pbkdf2_sha256$320000$dntuZiMwPMWYDHScZrCjzC$WNqtixLOERhJtBdyE195NqrK+/L3ArI4h85O5trNoJ0=', ## user12345
            last_login=None,
            username=name.replace(' ', '_').lower(),
            email=name.replace(' ', '_').lower()+'@gmail.com',
            is_active=True,
            first_name=name.split(' ')[-2],
            last_name=name.split(' ')[-1],
            is_staff=False,
            date_joined='2022-06-13T03:38:39Z',
            administrador=False
        )
        return user


    def handle(self, *args, **kwargs):
        '''
        Responsavel por executar o comando em si "python manage.py populate_database"
        '''

        random_quantity = random.randint(50, 1500)
        print('gerando registros: ', random_quantity)
        igreja = UnidadeOrganizacao.objects.get(nome="Igreja")
        produtos = list(Produto.objects.all())

        def handler_users():
            data = [self.generate_fake_users() for i in range(random_quantity)]
            User.objects.bulk_create(data, ignore_conflicts=True)

        def handler_doacoes_agendadas():
            users = list(User.objects.all()) 
            data = [self.generate_fake_doacoes_agendadas(produtos, igreja, users) for i in range(random_quantity)]
            DoacaoAgendada.objects.bulk_create(data, ignore_conflicts=True)

        def handler_doacao_recebida():
            ## pega todos agendados pendentes
            users_agendados_pendentes = list(DoacaoAgendada.objects.filter(status='PEN'))

            data = [self.generate_fake_doacoes_recebidas(produtos, igreja, users_agendados_pendentes) for i in range(random_quantity)]
            DoacaoRecebida.objects.bulk_create(data, ignore_conflicts=True)

        ## must be this order to generate fake data
        ## users -> agendadas -> recebidas
        handler_users()
        handler_doacoes_agendadas()
        handler_doacao_recebida()

