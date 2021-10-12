from django.http import Http404

from pages.models import UnidadeOrganizacao

class UnidadeOrganizacaoService():

    def getRecord():
        try:
            return UnidadeOrganizacao.objects.get(pk=1)
        except UnidadeOrganizacao.DoesNotExist:
            print('\n' + '*' * 40)
            print('*** UNIDADE ORGANIZAÇÃO NÃO DEFINIDA ***')
            print('*' * 40 + '\n')
            raise Http404
