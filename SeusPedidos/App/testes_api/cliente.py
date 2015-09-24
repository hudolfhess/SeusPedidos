from django.core.management import call_command
import json
from django.test import Client
from django.utils import unittest


__author__ = 'hcassus'

class TestesApiCliente(unittest.TestCase):

    def  setUp(self):
        self.c = Client()
        call_command('flush', interactive=False, verbosity=0)
        call_command('loaddata', 'base.json', verbosity=0)

    def teste_obter_lista_clientes(self):

        response = self.c.get('/api/cliente/')
        object_response = json.loads(response.content)

        assert response.status_code == 200
        assert object_response[1]['fields']['nome'] == 'Hudolf Hess'
        assert object_response[1]['fields']['email'] == 'hudolf@meuspedidos.com.br'

    def teste_cadastrar_cliente(self):

        self.c.post('/api/cliente',{'nome':'Henrique Cassus','email':'henrique.casssus@meuspedidos.com.br'})

        response = self.c.get('/api/cliente/')
        object_response = json.loads(response.content)

        assert response.status_code == 200
        assert object_response[2]['pk'] == 3
        assert object_response[2]['fields']['nome'] == 'Henrique Cassus'
        assert object_response[2]['fields']['email'] == 'henrique.casssus@meuspedidos.com.br'

    def teste_remover_cliente(self):

        self.c.delete('/api/cliente',{'id':'2'})

        response = self.c.get('/api/cliente/')
        object_response = json.loads(response.content)

        assert response.status_code == 200
        assert len(object_response) == 1
        assert object_response[0]['fields']['nome'] == 'Maria Helena Tiergarten'
        assert object_response[0]['fields']['email'] == 'maria@meuspedidos.com.br'

    def teste_atualizar_cliente(self):

        self.c.post('/api/cliente',{'id':'1','nome':'Maria Helena Tiergarten Amarante','email':'maria@meuspedidos.com.br'})

        response = self.c.get('/api/cliente/')
        object_response = json.loads(response.content)

        assert response.status_code == 200
        assert object_response[0]['pk'] == 1
        assert object_response[0]['fields']['nome'] == 'Maria Helena Tiergarten Amarante'
        assert object_response[0]['fields']['email'] == 'maria@meuspedidos.com.br'

