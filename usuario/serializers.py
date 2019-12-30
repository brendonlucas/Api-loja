from django.contrib.auth.models import User
from rest_framework import serializers
from usuario.models import Funcionario


class FuncionarioSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="Funcionario-detail")

    class Meta:
        model = Funcionario
        fields = ('url', 'pk', 'name', 'cpf', 'telefone')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class AddFuncionarioSerializer(serializers.ModelSerializer):
    funcionario_complement = UserSerializer()

    class Meta:
        model = Funcionario
        fields = ('name', 'cpf', 'telefone', 'funcionario_complement')
