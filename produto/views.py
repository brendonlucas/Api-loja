from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from produto.models import Produto
from produto.serializers import *


class ProdutoList(generics.ListCreateAPIView):
    queryset = Produto.objects.all().exclude(excluido=1)
    serializer_class = ProdutoSerializer
    name = 'Produto-list'


class ProdutoDetail(APIView):
    queryset = Produto.objects.all().exclude(excluido=1)
    serializer_class = ProdutoDetailSerializer
    name = 'Produto-detail'

    def get_object(self, pk):
        try:
            return Produto.objects.get(pk=pk)
        except Produto.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        queryset = self.get_object(pk)
        serializer = ProdutoDetailSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        queryset = self.get_object(pk)
        serializer = ProdutoDetailSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        produto = Produto.objects.get(pk=pk)
        produto.excluido = 1
        produto.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

