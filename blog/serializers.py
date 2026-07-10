from rest_framework import serializers
from .models import Artigo, Categoria


class ArtigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artigo
        fields = [
            'id',
            'autor',
            'titulo',
            'categoria',
            'conteudo',
            'imagem',
            'data_publicacao'
        ]


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']