from django.urls import path

from .views import Doar, MapaDoacao, ProdutosDoacao

app_name = 'doacaoapi'

urlpatterns = [
    path('grupo/<int:pk>', ProdutosDoacao.as_view(), name='produto_list'),
    path('doar/<int:pk>', Doar.as_view(), name='doar'),
    path('', MapaDoacao.as_view(), name='list'),
]
