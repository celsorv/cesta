from datetime import date, timedelta
from unittest import skip
from django.test import TestCase
from django.urls import reverse
from doacao.forms import AgendamentoForm
from pages.models import DoacaoAgendada, DoacaoRecebida, Produto, UnidadeOrganizacao
from recebimento.forms import EntradaAgendadaForm
from users.models import User

@skip('salta')
class DoacaoAgendadaCreateViewTest(TestCase):

  fixtures = ['data.json']  # insere dados no banco de dados de testes

  def setUp(self):
    self.doacao_id = 1
    self.data_post = {'produto': 1, 'quantidade': 1}
    # login de usuário antes de executar os testes
    self.login = self.client.login(email='gerencia@gmail.com', password='12345')

  def test_show_form_on_get(self):
    # garante que url está acessível e que template usado é o esperado
    response = self.client.get(reverse('doacao:doar', args=(self.doacao_id, )))
    self.assertEquals(200, response.status_code)
    self.assertTemplateUsed(response, 'doacao/doacao_form.html')

  def test_has_form_on_context(self):
    # garante que o formulário usado é o esperado
    response = self.client.get(reverse('doacao:doar', args=(self.doacao_id, )))
    self.assertIsInstance(response.context['form'], AgendamentoForm)

  def test_show_form_with_errors(self):
    # garante que erros são gerados quando enviando dados em branco
    response = self.client.post(reverse('doacao:doar', args=(self.doacao_id, )), data={})
    self.assertEquals(200, response.status_code)
    self.assertTemplateUsed(response, 'doacao/doacao_form.html')
    self.assertIsInstance(response.context['form'], AgendamentoForm)
    self.assertTrue(response.context['form'].errors)

  def test_save_new_doacao_agendada(self):
    self.assertEqual(DoacaoAgendada.objects.count(), 0)
    self.client.post(reverse('doacao:doar', args=(self.doacao_id, )), self.data_post)
    self.assertEqual(DoacaoAgendada.objects.count(), 1)

  def test_redirects_after_save(self):
    response = self.client.post(reverse('doacao:doar', args=(self.doacao_id, )), self.data_post)
    self.assertRedirects(response, reverse('doacao:doacao_ok'))

@skip('salta')
class DoacaoDiretaRecebidaCreateViewTest(TestCase):

  fixtures = ['data.json']  # insere dados no banco de dados de testes

  def setUp(self):
    # login de usuário antes de executar os testes
    self.login = self.client.login(email='gerencia@gmail.com', password='12345')

  def test_show_form_on_get(self):
    # garante que url está acessível e que template usado é o esperado
    response = self.client.get(reverse('recebimento:direta'))
    self.assertEquals(200, response.status_code)
    self.assertTemplateUsed(response, 'recebimento/recebimento_form.html')

  def test_has_form_on_context(self):
    # garante que o formulário usado é o esperado
    response = self.client.get(reverse('recebimento:direta'))
    self.assertIsInstance(response.context['form'], EntradaAgendadaForm)

  def test_show_form_with_errors(self):
    # garante que erros são gerados quando enviando dados em branco
    response = self.client.post(reverse('recebimento:direta'), data={})
    self.assertEquals(200, response.status_code)
    self.assertTemplateUsed(response, 'recebimento/recebimento_form.html')
    self.assertIsInstance(response.context['form'], EntradaAgendadaForm)
    self.assertTrue(response.context['form'].errors)

  def test_save_new_doacao_recebida(self):
    data_post = self.__create_data_post()
    self.assertEqual(DoacaoRecebida.objects.count(), 0)
    self.client.post(reverse('recebimento:direta'), data_post)
    self.assertEqual(DoacaoRecebida.objects.count(), 1)

  def test_redirects_after_save(self):
    data_post = self.__create_data_post()
    response = self.client.post(reverse('recebimento:direta'), data_post)
    self.assertRedirects(response, reverse('recebimento:list'))

  def __create_data_post(self):
     return {
      'doador': 102,
      'produto': 1, 
      'quantidade': 1, 
      'dataRecebimento': date.today(),
      'dataValidade': date.today() + timedelta(days=15)
    }

@skip('salta')
class DoacaoAgendadaRecebidaCreateViewTest(TestCase):

  fixtures = ['data.json']  # insere dados no banco de dados de testes

  def setUp(self):
    self.doacao_id = 1
    # login de usuário antes de executar os testes
    self.login = self.client.login(email='gerencia@gmail.com', password='12345')

  def test_show_form_on_get(self):
    # garante que url está acessível e que template usado é o esperado
    self.__create_doacao_agendada()
    response = self.client.get(reverse('recebimento:agendada', args=(self.doacao_id, )))
    self.assertEquals(200, response.status_code)
    self.assertTemplateUsed(response, 'recebimento/recebimento_form.html')

  def test_has_form_on_context(self):
    # garante que o formulário usado é o esperado
    self.__create_doacao_agendada()
    response = self.client.get(reverse('recebimento:agendada', args=(self.doacao_id, )))
    self.assertIsInstance(response.context['form'], EntradaAgendadaForm)

  def test_show_form_with_errors(self):
    # garante que erros são gerados quando enviando dados em branco
    self.__create_doacao_agendada()
    response = self.client.post(reverse('recebimento:agendada', args=(self.doacao_id, )), data={})
    self.assertEquals(200, response.status_code)
    self.assertTemplateUsed(response, 'recebimento/recebimento_form.html')
    self.assertIsInstance(response.context['form'], EntradaAgendadaForm)
    self.assertTrue(response.context['form'].errors)

  def test_save_new_doacao_recebida(self):
    # garante que doação recebida pode ser criada
    self.__create_doacao_agendada()
    data_post = self.__create_data_post()
    self.assertEqual(DoacaoRecebida.objects.count(), 0)
    self.client.post(reverse('recebimento:agendada', args=(self.doacao_id, )), data=data_post)
    self.assertEqual(DoacaoRecebida.objects.count(), 1)

  def test_redirects_after_save(self):
    # garante que após doação recebida ser criada, há o redirecionamento esperado
    self.__create_doacao_agendada()
    data_post = self.__create_data_post()
    response = self.client.post(reverse('recebimento:agendada', args=(self.doacao_id, )), data=data_post)
    print(response['content-type'])
    self.assertRedirects(response, reverse('recebimento:list'))

  def __create_data_post(self):
     return {
      'doador': 102,
      'produto': 1, 
      'quantidade': 1, 
      'dataRecebimento': date.today(),
      'dataValidade': date.today() + timedelta(days=15)
    }

  def __create_doacao_agendada(self):
    doador = User.objects.get(pk=102)
    produto = Produto.objects.get(pk=1)
    DoacaoAgendada.objects.create(
      doador=doador,
      produto=produto,
      dataAgendamento=date.today()
    )
