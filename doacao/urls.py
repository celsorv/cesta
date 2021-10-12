from django.urls import path

from .views import AgendamentoList, AgendamentoCreate, AgendamentoOk

app_name = 'doacao'

urlpatterns = [
    path('', AgendamentoList.as_view(), name='list'),
    path('doar/<int:pk>/', AgendamentoCreate.as_view(), name='doar'),
    path('ok$0bf082$03af301/', AgendamentoOk.as_view(), name='doacao_ok'),
]
