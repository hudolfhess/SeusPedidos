from django.db import models, transaction

class Pedido(models.Model):
    cliente = models.ForeignKey('Cliente')
    status = models.IntegerField()
    data_hora = models.DateTimeField()
