from datetime import date, timedelta
from django.test import TestCase
from pages.models import DoacaoAgendada, DoacaoRecebida, Produto
from users.models import User
from django.core.exceptions import ValidationError

class DoacaoAgendadaModelTest(TestCase):

  fixtures = ['data.json']  # insere dados no banco de dados de testes

  def setUp(self):
    doador = User.objects.get(pk=102)
    produto = Produto.objects.get(pk=1)
    self.data = {
      'doador': doador,
      'produto': produto,
    }

  def test_create_new_doacao_agendada(self):
    r = DoacaoAgendada.objects.create(**self.data)
    self.assertEquals(r.dataAgendamento, date.today())
    self.assertEquals(r.unidadeOrganizacao.id, 1)

  def test_quantity_must_be_greater_than_zero(self):
    record = DoacaoAgendada.objects.create(**self.data)
    record.quantidade = 0
    with self.assertRaises(ValidationError) as e:
      record.full_clean()
    self.assertIn('quantidade', e.exception.message_dict)

  def test_status_must_be_in_list(self):
    record = DoacaoAgendada.objects.create(**self.data)
    record.status = 'ZZZ'
    with self.assertRaises(ValidationError) as e:
      record.full_clean()
    self.assertIn('status', e.exception.message_dict)

  def test_non_unique_fields(self):
    DoacaoAgendada.objects.create(**self.data)
    DoacaoAgendada.objects.create(**self.data)
    self.assertEqual(DoacaoAgendada.objects.count(), 2)


class DoacaoRecebidaModelTest(TestCase):

  fixtures = ['data.json']  # insere dados no banco de dados de testes

  def setUp(self):
    doador = User.objects.get(pk=102)
    produto = Produto.objects.get(pk=1)
    self.data = {
      'doador': doador,
      'produto': produto,
      'dataValidade': date.today()
    }

  def test_create_new_doacao_agendada(self):
    r = DoacaoRecebida.objects.create(**self.data)
    self.assertEquals(r.dataRecebimento, date.today())
    self.assertEquals(r.unidadeOrganizacao.id, 1)

  def test_quantity_must_be_greater_than_zero(self):
    record = DoacaoRecebida.objects.create(**self.data)
    record.quantidade = 0
    with self.assertRaises(ValidationError) as e:
      record.full_clean()
    self.assertIn('quantidade', e.exception.message_dict)

  def test_expiration_date_must_be_greater_than_or_equal_to_current(self):
    record = DoacaoRecebida.objects.create(**self.data)
    record.dataValidade = date.today() - timedelta(days=1)
    with self.assertRaises(ValidationError) as e:
      record.full_clean()
    self.assertIn('dataValidade', e.exception.message_dict)

  def test_status_must_be_in_list(self):
    record = DoacaoRecebida.objects.create(**self.data)
    record.status = 'ZZZ'
    with self.assertRaises(ValidationError) as e:
      record.full_clean()
    self.assertIn('status', e.exception.message_dict)

  def test_non_unique_fields(self):
    DoacaoRecebida.objects.create(**self.data)
    DoacaoRecebida.objects.create(**self.data)
    self.assertEqual(DoacaoRecebida.objects.count(), 2)


