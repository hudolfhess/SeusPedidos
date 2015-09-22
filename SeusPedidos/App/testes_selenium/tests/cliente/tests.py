from django.utils import unittest
from selenium import webdriver
from SeusPedidos.App.testes_selenium.steps.acoes_cliente import AcoesCliente

__author__ = 'hcassus'


class TestesCliente(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.acoes_cliente = AcoesCliente(self.driver)


    def teste_cadastro_cliente_valido(self):
        self.acoes_cliente\
            .acessar_pagina()\
                .contar_clientes()\
                .cadastrar_cliente('Henrique Cassus','henrique.cassus@meuspedidos.com.br')\
                .verificar_mensagem_sucesso()\
                .verificar_diferenca_numero_clientes(1)\
                .validar_ultimo_cliente()

    def teste_remocao_ultimo_cliente(self):
        self.acoes_cliente\
            .acessar_pagina()\
                .contar_clientes()\
                .remover_ultimo_cliente()\
                .verificar_diferenca_numero_clientes(-1)\


    @classmethod
    def tearDownClass(self):
        self.driver.quit()