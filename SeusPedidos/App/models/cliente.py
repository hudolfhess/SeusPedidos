from django.db import models, transaction

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)