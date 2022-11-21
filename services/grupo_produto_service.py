from pages.models import GrupoProduto, Produto

class GrupoProdutoService():
    
    def getById(self, pk):
        return GrupoProduto.objects.get(pk=pk)
