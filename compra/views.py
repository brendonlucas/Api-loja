from rest_framework import generics, status
from rest_framework.response import Response

from compra.models import Compra
from compra.serializers import *
from produto.models import Produto
from usuario.models import Funcionario


class CompraList(generics.ListCreateAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    name = 'Compra-list'


class CompraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    name = 'Compra-detail'


class ProdutoCompra(generics.GenericAPIView):
    queryset = Compra.objects.all()
    serializer_class = FazerCompraSerializer
    name = 'Produto-Compra'

    def post(self, request, id_produto, *args, **kwargs):
        # if request.user.is_authenticated:
        try:
            produto = Produto.objects.get(id=id_produto)
            qtd = request.data['quantidade']
        except Produto.DoesNotExist:
            return Response({'erro': "HTTP_404_NOT_FOUND"}, status=status.HTTP_404_NOT_FOUND)

        if qtd <= produto.quantidade:
            valor_total = produto.preco * qtd
            produto.quantidade = produto.quantidade - qtd
            compra = Compra(produto=produto, quantidade=qtd,
                            valor_total=valor_total)
            produto.save()
            compra.save()
            return Response(status=status.HTTP_200_OK)
