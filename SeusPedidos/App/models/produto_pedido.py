from django.db import models, transaction

class Produto_Pedido(models.Model):
    pedido = models.ForeignKey('Pedido')
    produto = models.ForeignKey('Produto')
    desconto = models.DecimalField(max_digits=3, decimal_places=2)
    quantidade = models.IntegerField()
    valor_unidade = models.DecimalField(max_digits=8, decimal_places=2)
