from django.core.management import call_command
import json
from django.test import Client
from django.utils import unittest


__author__ = 'hcassus'

class TestesApiProduto(unittest.TestCase):

    def setUp(self):
        self.c = Client()
        call_command('flush', interactive=False, verbosity=0)
        call_command('loaddata', 'base.json', verbosity=0)

    def teste_obter_lista_produtos(self):

        response = self.c.get('/api/produto/')
        object_response = json.loads(response.content)

        assert response.status_code == 200
        assert object_response[1]['fields']['nome'] == 'iPad Air 2'
        assert object_response[1]['fields']['valor'] == 3500.0

    def teste_cadastrar_produto(self):

        self.c.post('/api/produto',{'nome':'Produto Teste','valor':'2500'})

        response = self.c.get('/api/produto/')
        object_response = json.loads(response.content)

        assert response.status_code == 200
        assert object_response[2]['fields']['nome'] == 'Produto Teste'
        assert object_response[2]['fields']['valor'] == 2500.0

    def teste_remover_produto(self):

        self.c.delete('/api/produto',{'id':'2'})

        response = self.c.get('/api/produto/')
        object_response = json.loads(response.content)

        assert response.status_code == 200
        assert len(object_response) == 1
        assert object_response[0]['pk'] == 1
        assert object_response[0]['fields']['nome'] == 'Mac Book 256GB Intel Core M'
        assert object_response[0]['fields']['valor'] == 8499.0

    def teste_atualizar_produto(self):

        self.c.post('/api/produto',{'id':'2','nome':'iPad Mini 2','valor':'2499'})

        response = self.c.get('/api/produto/')
        object_response = json.loads(response.content)

        assert response.status_code == 200
        assert object_response[1]['pk'] == 2
        assert object_response[1]['fields']['nome'] == 'iPad Mini 2'
        assert object_response[1]['fields']['valor'] == 2499.0

