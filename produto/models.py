from django.db import models
from django.contrib.auth.models import User


class Produto(models.Model):
    name = models.CharField(max_length=250)
    preco = models.FloatField()
    quantidade = models.IntegerField()
    excluido = models.BooleanField(default=0)
    file = models.FileField(blank=False, null=True)



