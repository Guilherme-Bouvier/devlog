from django.shortcuts import render, get_object_or_404, redirect

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .models import Artigo, Categoria
from .forms import ContatoForm
from .serializers import ArtigoSerializer, CategoriaSerializer



def home(request):

    categoria_selecionada = request.GET.get('categoria')
    categorias = Categoria.objects.all()

    # ==========================================
    # FILTRO (SE JÁ EXISTE, MANTIDO)
    # ==========================================
    if categoria_selecionada:
        noticias = Artigo.objects.filter(categoria__nome__icontains=categoria_selecionada)
    else:
        noticias = Artigo.objects.all()

    # ordenação (IMPORTANTE para consistência)
    noticias = noticias.order_by('-data_publicacao')

    # ==========================================
    # ⭐ NOVOS DADOS PARA A HOME (SEM REMOVER NADA)
    # ==========================================
    artigos_destaque = noticias[:4]   # cards superiores
    banner_artigos = noticias[:5]     # banner principal

    contexto = {
        # original (não mexido)
        'lista_artigos': noticias,

        # categorias (original)
        'lista_categorias': categorias,

        # filtro atual (original)
        'categoria_selecionada': categoria_selecionada,

        # ⭐ NOVO (adicionado)
        'artigos_destaque': artigos_destaque,

        # 📰 NOVO (adicionado)
        'banner_artigos': banner_artigos,
    }

    return render(request, "blog/index.html", contexto)


def sobre_nos(request):
    categorias = Categoria.objects.all()

    contexto = {
        'lista_categorias': categorias
    }

    return render(request, "blog/sobre.html", contexto)


def artigo_detalhe(request, id):
    categorias = Categoria.objects.all()

    noticia = get_object_or_404(Artigo, id=id)

    contexto = {
        'lista_categorias': categorias,
        'artigo': noticia
    }

    return render(request, 'blog/artigo_detalhe.html', contexto)


def uc1(request):
    return render(request, "blog/uc1.html")


def uc2(request):
    return render(request, "blog/uc2.html")


def uc3(request):
    return render(request, "blog/uc3.html")


def uc4(request):
    return render(request, "blog/uc4.html")


def uc5(request):
    return render(request, "blog/uc5.html")


def fale_conosco(request):
    
    categorias = Categoria.objects.all()


    if request.method == "POST":
        formulario = ContatoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('home')

    else:
        formulario = ContatoForm()
    
    contexto = {
        'lista_categorias': categorias,
        'form': formulario
    }

    return render(request, 'blog/contato.html', contexto)


@api_view(['GET'])
def api_listar_artigos(request):

    artigos = Artigo.objects.all()
    serializer = ArtigoSerializer(artigos, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def api_listar_categorias(request):

    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)

    return Response(serializer.data)

# A FECHADURA: Só entra se mostrar o Cartão Magnético (token):
@api_view(['POST'])
@permission_classes([IsAuthenticated])

def api_criar_artigo(request):
    #Recebemos os dados digitados e passamos para o Serializer 
    serializer = ArtigoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save() # Salva no PostgreSQL
        return Response(serializer.data, status=201) # 201 Created
    
    return Response(serializer.errors, status=400) # 400 Bad Request