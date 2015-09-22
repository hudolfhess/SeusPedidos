from django.utils import unittest
from selenium import webdriver
from SeusPedidos.App.testes_selenium.steps.acoes_pedido import AcoesPedido

__author__ = 'hcassus'


class TestesPedido(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.acoes_pedido = AcoesPedido(self.driver)

    def teste_cadastro_pedido_valido(self):
        self.acoes_pedido\
            .acessar_pagina()\
                .contar_pedidos()\
                .cadastrar_pedido('Hudolf Hess', [('MacBook Air',10,5),('iPad 16GB',10,0)])\
                .verificar_diferenca_numero_pedidos(1)\
                .validar_ultimo_pedido()

    def teste_remocao_ultimo_produto(self):
        self.acoes_pedido\
            .acessar_pagina()\
                .contar_pedidos()\
                .remover_ultimo_pedido()\
                .verificar_diferenca_numero_pedidos(-1)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()