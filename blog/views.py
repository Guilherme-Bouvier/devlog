#Importamos a ferramenta para devolver texto simples
from django.http import HttpResponse
from django.shortcuts import render

#Criamos a nossa função para a página inicial
def home(request):

    #Devcolvemos a resposta (o prato pronto)
    return render(request, 'blog/index.html')

def sobre_nos(request):

    #O 'request' é o pedido (comando) do usuário.
    mensagem = "<h1>Sobre o DevBlog!</h1>"

    #Devcolvemos a resposta (o prato pronto)
    return render(request, 'blog/sobre.html')