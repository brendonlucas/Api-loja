from django.shortcuts import render
from rest_framework import generics

from usuario.models import Funcionario
from usuario.serializers import *


class FuncionarioList(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    name = 'Funcionario-list'


class FuncionarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    name = 'Funcionario-detail'


class FuncinarioAdd(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = AddFuncionarioSerializer
    name = 'Add-Funcionario'

    def post(self, request, *args, **kwargs):
        user = User.objects.create_user(username=request.data['username'], password=request.data['password'],
                                        email=request.data['email'])
        funcionario = Funcionario(name=request.data['name'], cpf=request.data['cpf'], telefone=request.data['telefone'],
                                  funcionario_complement=user)
        funcionario.save()
