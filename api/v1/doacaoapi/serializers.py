from rest_framework import serializers
from pages.models import DoacaoAgendada, Produto

class MapaDoacaoSerializer(serializers.Serializer):

  id = serializers.IntegerField()
  descricao = serializers.CharField()
  percentual = serializers.IntegerField()


class ProdutosDoacaoSerializer(serializers.ModelSerializer):

  class Meta:
    model = Produto
    fields = ('id', 'descricao', )


class ProdutosForeignKey(serializers.PrimaryKeyRelatedField):

  def get_queryset(self):
    grupo = self.context['grupo']
    queryset = super(ProdutosForeignKey, self).get_queryset()
    if not grupo or not queryset:
      return None
    return queryset.filter(grupoProduto=grupo)


class DoacaoAgendadaSerializer(serializers.ModelSerializer):

  produto = ProdutosForeignKey(queryset=Produto.objects)

  class Meta:
    model = DoacaoAgendada
    fields = ('produto', 'quantidade', )

  def save(self, **kwargs):
    user = self.context['request'].user
    return super().save(doador=user, **kwargs)

