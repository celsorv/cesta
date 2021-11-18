from django.http import Http404

from pages.models import UnidadeOrganizacao

class UnidadeOrganizacaoService():

    def getRecord():

        obj = None

        orj, created = UnidadeOrganizacao.objects.get_or_create(
                id = 1,
                nome = 'Matriz São José Operário',
                ativo = True,
                metaQtdeCestas = 10,
                diasEsperaAgendadas = 10
        )

        return obj
