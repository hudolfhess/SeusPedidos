from django.db import models, transaction

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=8, decimal_places=2)