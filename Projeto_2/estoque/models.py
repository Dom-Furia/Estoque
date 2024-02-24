from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.FloatField()
    quantidade = models.IntegerField()
    descricao = models.CharField(max_length=200)
