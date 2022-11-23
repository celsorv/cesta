from django.urls import path

from .views import FamiliaAtendidaCreate, FamiliaAtendidaDelete, FamiliaAtendidaEdit, FamiliaAtendidaList
from .views import GrupoProdutoList, GrupoProdutoEdit, GrupoProdutoCreate, GrupoProdutoDelete, FamiliaAtendidaQuestionario
from .views import UnidadeOrganizacaoEdit, ProdutoList, ProdutoEdit, ProdutoCreate, ProdutoDelete

app_name = 'cadastros'

urlpatterns = [
    path('unidadeorg/<int:pk>/', UnidadeOrganizacaoEdit.as_view(), name='unidade_org_edit'),
    path('familiaatendida/', FamiliaAtendidaList.as_view(), name='familia_atendida_list'),
    path('familiaatendida/novo', FamiliaAtendidaCreate.as_view(), name='familia_atendida_create'),
    path('familiaatendida/<int:pk>/', FamiliaAtendidaEdit.as_view(), name='familia_atendida_edit'),
    path('familiaatendida/<int:pk>/delete', FamiliaAtendidaDelete.as_view(), name='familia_atendida_delete'),
    path('familiaatendida/<int:pk>/questionario', FamiliaAtendidaQuestionario.as_view(), name='familia_atendida_question'),
    path('grupoproduto/', GrupoProdutoList.as_view(), name='grupo_produto_list'),
    path('grupoproduto/novo', GrupoProdutoCreate.as_view(), name='grupo_produto_create'),
    path('grupoproduto/<int:pk>/', GrupoProdutoEdit.as_view(), name='grupo_produto_edit'),
    path('grupoproduto/<int:pk>/delete', GrupoProdutoDelete.as_view(), name='grupo_produto_delete'),
    path('produto/', ProdutoList.as_view(), name='produto_list'),
    path('produto/novo', ProdutoCreate.as_view(), name='produto_create'),
    path('produto/<int:pk>/', ProdutoEdit.as_view(), name='produto_edit'),
    path('produto/<int:pk>/delete', ProdutoDelete.as_view(), name='produto_delete'),
]
