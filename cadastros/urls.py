from django.urls import path

from .views import GrupoProdutoList, GrupoProdutoEdit, GrupoProdutoCreate, GrupoProdutoDelete
from .views import ProdutoList, ProdutoEdit, ProdutoCreate, ProdutoDelete

app_name = 'cadastros'

urlpatterns = [
    path('grupoproduto/', GrupoProdutoList.as_view(), name='grupo_produto_list'),
    path('grupoproduto/novo', GrupoProdutoCreate.as_view(), name='grupo_produto_create'),
    path('grupoproduto/<int:pk>/', GrupoProdutoEdit.as_view(), name='grupo_produto_edit'),
    path('grupoproduto/<int:pk>/delete', GrupoProdutoDelete.as_view(), name='grupo_produto_delete'),
    path('produto/', ProdutoList.as_view(), name='produto_list'),
    path('produto/novo', ProdutoCreate.as_view(), name='produto_create'),
    path('produto/<int:pk>/', ProdutoEdit.as_view(), name='produto_edit'),
    path('produto/<int:pk>/delete', ProdutoDelete.as_view(), name='produto_delete'),
]
