from rest_framework import serializers

from produto.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="Produto-detail")

    class Meta:
        model = Produto
        fields = ('url', 'pk', 'name', 'preco', 'quantidade')


class ProdutoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('pk', 'name', 'preco', 'quantidade')
