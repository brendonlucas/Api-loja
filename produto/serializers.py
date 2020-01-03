from rest_framework import serializers

from produto.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = ('pk', 'name', 'preco', 'quantidade', 'file', 'descricao')


class ProdutoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('pk', 'name', 'preco', 'quantidade', 'descricao')
