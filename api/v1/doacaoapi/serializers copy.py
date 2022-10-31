from rest_framework import serializers
from pages.models import DoacaoAgendada, Produto

class MapaDoacaoSerializer(serializers.Serializer):

  id = serializers.IntegerField()
  descricao = serializers.CharField()
  percentual = serializers.IntegerField()


class ProdutosDoacaoSerializer(serializers.ModelSerializer):

  class Meta:
    model = Produto
    fields = ('id', 'descricao' )


class ProdutosForeignKey(serializers.PrimaryKeyRelatedField):

    def get_queryset(self):
      grupo = self.context['grupo']
      return Produto.objects.filter(grupoProduto=grupo)


class DoacaoAgendadaSerializer(serializers.ModelSerializer):

  produto = ProdutosForeignKey(many=True)

  """
  produto = serializers.PrimaryKeyRelatedField(
    queryset=Produto.objects.filter(grupoProduto=self.context['grupo'])
  )
  """

  class Meta:
    model = DoacaoAgendada
    fields = ('produto', 'quantidade', )


  
"""
  produto = serializers.PrimaryKeyRelatedField(
    queryset=Produto.objects.filter(grupoProduto=self.context['grupo'])
  )
"""




"""
class UserDishForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        user = self.context['request'].user
        return Dish.objects.filter(user=user)


class MenuCreateSerializer(serializers.ModelSerializer):
    dish = UserDishForeignKey(many=True)

    class Meta:
        model = Menu
        fields = ['title', 'description', 'dish', 'price', ]
        read_only_fields = ['user', ]

    def get_user(self, obj):
        return str(obj.user.username)

"""