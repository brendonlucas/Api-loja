from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters

from rest_framework.parsers import FileUploadParser

from produto.models import Produto
from produto.serializers import *


class ProdutoList(generics.ListCreateAPIView):
    queryset = Produto.objects.all().exclude(excluido=1)
    serializer_class = ProdutoSerializer
    parser_class = (FileUploadParser,)
    name = 'Produto-list'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            file_serializer = ProdutoSerializer(data=request.data)
            if file_serializer.is_valid():
                print(request.data['file'])
                file_serializer.save()
                return Response(file_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':'sem autorizacao'}, status=status.HTTP_401_UNAUTHORIZED)


class ProdutoDetail(generics.RetrieveUpdateAPIView):
    queryset = Produto.objects.all().exclude(excluido=1)
    serializer_class = ProdutoSerializer
    name = 'Produto-detail'


class ProdutoDetailDeleteUpdate(APIView):
    queryset = Produto.objects.all().exclude(excluido=1)
    serializer_class = ProdutoDetailSerializer
    name = 'Produto-detail-delete-update'
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request, pk, *args, **kwargs):
        produto = Produto.objects.get(pk=pk)
        produto.excluido = 1
        produto.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, *args, **kwargs):
        produto = Produto.objects.get(pk=pk)
        produto.name = request.data['name']
        produto.quantidade = request.data['quantidade']
        produto.preco = request.data['preco']
        produto.descricao = request.data['descricao']
        produto.save()
        return Response(request.data, status=status.HTTP_200_OK)


class GetNewProdutsList(generics.ListAPIView):
    queryset = Produto.objects.all().exclude(excluido=1).order_by('-id')[:10]
    serializer_class = ProdutoSerializer
    name = 'Produto-list'

