from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('produtos_grafico/', views.produtos_mais_doados, name='produtos_grafico'),
    path('cestas_doadas/', views.cestas_doadas, name='cestas_doadas'),
    path('renda_familiar/', views.renda_familiar, name='renda_familiar'),

]