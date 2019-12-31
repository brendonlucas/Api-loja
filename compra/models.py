from django.db import models
from produto.models import Produto
from usuario.models import Funcionario


class Compra(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_compra = models.DateField(auto_now_add=True)
    quantidade = models.IntegerField()
    valor_total = models.FloatField()



