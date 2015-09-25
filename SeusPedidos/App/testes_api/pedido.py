from django.core.management import call_command
import json
from django.core import serializers
from django.test import Client
from django.utils import unittest


__author__ = 'hcassus'

class TestesApiPedido(unittest.TestCase):

    def  setUp(self):
        self.c = Client()
        call_command('flush', interactive=False, verbosity=0)
        call_command('loaddata', 'base.json', verbosity=0)

    def teste_obter_lista_pedidos(self):
        response = self.c.get('/api/pedido/')
        object_response = json.loads(response.content)

        #[{"cliente_id": 1, "status": 1, "status_description": "Em aberto", "cliente": {"id": "Maria Helena Tiergarten", "nome": "Maria Helena Tiergarten"}, "itens": [{"quantidade": 2, "valor_unidade": "3500.00", "produto": {"valor": "3500.00", "id": 2, "nome": "iPad Air 2"}, "id": 1, "desconto": 0}, {"quantidade": 4, "valor_unidade": "8499.00", "produto": {"valor": "8499.00", "id": 1, "nome": "Mac Book 256GB Intel Core M"}, "id": 2, "desconto": 10}], "data_hora": "23/09/2015 18:39:55", "total": "37596.40", "id": 1}]

        assert response.status_code == 200
        assert object_response[0]['cliente_id'] == 1
        assert object_response[0]['status'] == 1
        assert object_response[0]['status_description'] == 'Em aberto'
        assert object_response[0]['cliente']['id'] == 1
        assert object_response[0]['cliente']['nome'] == 'Maria Helena Tiergarten'
        assert len(object_response[0]['itens']) == 2
        assert object_response[0]['total'] == '37596.40'

    def teste_cadastrar_pedido(self):
        dados = {
            'cliente_id': 2,
            'itens': (
                {
                    'quantidade': 6,
                    'desconto': 10,
                    'produto': {
                        'id': 2,
                        'nome': 'iPad Air 2',
                        'valor': 3500,
                    },
                },
                {
                    'quantidade': 50,
                    'desconto': 10,
                    'produto': {
                        'id': 1,
                        'nome': 'Mac Book 256GB Intel Core M',
                        'valor': 8499,
                    },
                },
            )
        }

        #response_post = self.c.post('/api/pedido',{"cliente_id": 2, "itens": {0 : {"quantidade": 6, "produto": {"valor": "3500.00", "id": 2, "nome": "iPad Air 2"}, "desconto": 10}, 1: {"quantidade": 50, "valor_unidade": "8499.00", "produto": {"valor": "8499.00", "id": 1, "nome": "Mac Book 256GB Intel Core M"}, "desconto": 10}}})
        response_post = self.c.post('/api/pedido', dados)
        print response_post


        response = self.c.get('/api/pedido/')
        object_response = json.loads(response.content)

        assert response.status_code == 200
        assert object_response[1]['cliente_id'] == 2
        assert object_response[1]['status'] == 1
        assert object_response[1]['status_description'] == 'Em aberto'
        assert object_response[1]['cliente']['nome'] == 'Hudolf Hess'
        assert len(object_response[1]['itens']) == 2
        assert object_response[1]['total'] == '401355.00'

    def teste_remover_pedido(self):
        self.c.delete('/api/pedido',{'id':'2'})

        response = self.c.get('/api/pedido/')
        object_response = json.loads(response.content)

        assert response.status_code == 200
        assert object_response[0]['cliente_id'] == 1
        assert object_response[0]['status'] == 1
        assert object_response[0]['status_description'] == 'Em aberto'
        assert object_response[0]['cliente']['id'] == 1
        assert object_response[0]['cliente']['nome'] == 'Maria Helena Tiergarten'
        assert len(object_response[0]['itens']) == 2
        assert object_response[0]['total'] == '37596.40'

    def teste_atualizar_pedido(self):
        self.c.post('/api/pedido',{"cliente_id": 2, "itens": [{"quantidade": 6, "valor_unidade": "3500.00", "produto": {"valor": "3500.00", "id": 2, "nome": "iPad Air 2"}, "desconto": 10}, {"quantidade": 50, "valor_unidade": "8499.00", "produto": {"valor": "8499.00", "id": 1, "nome": "Mac Book 256GB Intel Core M"}, "desconto": 10}]})

        response = self.c.get('/api/pedido/')
        object_response = json.loads(response.content)

        assert response.status_code == 200
        assert object_response[0]['cliente_id'] == 1
        assert object_response[0]['status'] == 1
        assert object_response[0]['status_description'] == 'Em aberto'
        assert object_response[0]['cliente']['id'] == 2
        assert object_response[0]['cliente']['nome'] == 'Hudolf Hess'
        assert len(object_response[0]['itens']) == 2
        assert object_response[0]['total'] == '37596.40'
