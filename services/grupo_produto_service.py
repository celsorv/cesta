from pages.models import GrupoProduto

class GrupoProdutoService():
    
    def getById(self, pk):
        return GrupoProduto.objects.get(pk=pk)
        