from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.v1.doacaoapi.serializers import DoacaoAgendadaSerializer, MapaDoacaoSerializer, ProdutosDoacaoSerializer

from pages.models import Produto

from services.unidadeorg_service import UnidadeOrganizacaoService as orgService
from services.doacao_service import DoacaoService


class MapaDoacao(generics.ListAPIView):
  
    serializer_class = MapaDoacaoSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        itens = DoacaoService.itensCestas()
        serializer = MapaDoacaoSerializer(itens, many=True).data
        return serializer


class ProdutosDoacao(generics.ListAPIView):

    serializer_class = ProdutosDoacaoSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        itens = Produto.objects.filter(grupoProduto = pk)
        serializer = ProdutosDoacaoSerializer(itens, many=True).data
        return serializer


class Doar(generics.CreateAPIView):
    
    serializer_class = DoacaoAgendadaSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Produto.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'grupo': self.kwargs.get('pk')})

        return context


    def create(self, request, *args, **kwargs):
        organizacao = orgService.getRecord()
        request.data['unidadeOrganizacao'] = organizacao
       
        return super().create(request, *args, **kwargs)
