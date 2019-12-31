from rest_framework import serializers

from compra.models import Compra
from produto.models import Produto
from usuario.models import Funcionario


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id', 'name', 'preco', 'quantidade')


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('id', 'name', 'cpf', 'telefone')


class CompraSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer()

    class Meta:
        model = Compra
        fields = ('id', 'produto', 'data_compra', 'quantidade', 'valor_total')


class FazerCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ('quantidade',)
