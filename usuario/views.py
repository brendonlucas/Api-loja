from rest_framework.authtoken.models import Token

from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

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
    permission_classes = (permissions.IsAuthenticated,)


class FuncinarioAdd(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = AddFuncionarioSerializer
    name = 'Add-Funcionario'

    def post(self, request, *args, **kwargs):
        print(request.data)
        try:
            user = User.objects.get(username=request.data['username'])
            if user:
                return Response({'error': 'usuario ja existe'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:

            user = User.objects.create_user(username=request.data['username'], password=request.data['password'],
                                            email=request.data['email'])
            funcionario = Funcionario(name=request.data['name'], cpf=request.data['cpf'],
                                      telefone=request.data['telefone'],
                                      funcionario_complement=user)
            funcionario.save()
            return Response(status=status.HTTP_201_CREATED)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        dados_funcionario = get_object_or_404(Funcionario, funcionario_complement=user.id)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'name': dados_funcionario.name
        })
