from django.urls import path
from . import views                # Oponto (.) significa diretorio atual

#Criamos a lidta de rotas DESTE aplicativo
urlpatterns = [
    #path ('caminho', função_da_view, nome_apelido)
    #caminho vazio '' representa a página raiz
    path('', views.home, name='home'),
    path('sobre/', views.sobre_nos, name='sobre')


]
