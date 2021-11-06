from django.urls import path

from .views import RecebimentoList, RecebimentoCreate, RecebidosConsulta

app_name = 'recebimento'

urlpatterns = [
    path('', RecebimentoList.as_view(), name='list'),
    path('direta/', RecebimentoCreate.as_view(), name='direta'),
    path('agendada/<int:pk>/', RecebimentoCreate.as_view(), name='agendada'),
    path('produto/<int:pk>/', RecebidosConsulta.as_view(), name='produto_list'),
]
