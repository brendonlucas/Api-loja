from django.db import models
from django.contrib.auth.models import User


class Funcionario(models.Model):
    name = models.CharField(max_length=250)
    cpf = models.CharField(max_length=30)
    telefone = models.CharField(max_length=250)
    funcionario_complement = models.OneToOneField(User, on_delete=models.CASCADE, related_name='complemento')



