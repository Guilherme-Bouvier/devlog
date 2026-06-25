#Importamos a ferramenta para devolver texto simples
from django.http import HttpResponse

#Criamos a nossa função para a página inicial
def home(request):

    #O 'request' é o pedido (comando) do usuário.
    mensagem = "<h1>Bem-vindo ao DevBlog!</h1> <p>Em breve, artigos aqui.</p>"

    #Devcolvemos a resposta (o prato pronto)
    return HttpResponse(mensagem)

def sobre_nos(request):

    #O 'request' é o pedido (comando) do usuário.
    mensagem = "<h1>Sobre o DevBlog!</h1>"

    #Devcolvemos a resposta (o prato pronto)
    return HttpResponse(mensagem)