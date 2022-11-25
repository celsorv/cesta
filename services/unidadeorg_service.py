from pages.models import UnidadeOrganizacao

class UnidadeOrganizacaoService():

    def getRecord():
        
        try:
            obj = UnidadeOrganizacao.objects.get(pk=1)
        except UnidadeOrganizacao.DoesNotExist:
            obj = UnidadeOrganizacao(
                id = 1,
                nome = 'Matriz São José Operário',
                ativo = True,
                diasEsperaAgendadas = 10
            )
            obj.save()

        return obj
