from django.urls import path

from .views import AgendamentoList, AgendamentoDetail, AgendamentoCreate, AgendamentoOk, AgendadosConsulta

app_name = 'doacao'

urlpatterns = [
    path('', AgendamentoList.as_view(), name='list'),
    path('<int:pk>/ver', AgendamentoDetail.as_view(), name='view'),
    path('doar/<int:pk>/', AgendamentoCreate.as_view(), name='doar'),
    path('ok$0bf082$03af301/', AgendamentoOk.as_view(), name='doacao_ok'),
    path('produto/<int:pk>/', AgendadosConsulta.as_view(), name='produto_list'),
]
