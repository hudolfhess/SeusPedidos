from django.utils import unittest
from selenium import webdriver
from SeusPedidos.App.testes_selenium.steps.acoes_produto import AcoesProduto

__author__ = 'hcassus'


class TestesProduto(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.acoes_produto = AcoesProduto(self.driver)

    def teste_cadastro_produto_valido(self):
        self.acoes_produto\
            .acessar_pagina()\
                .contar_itens()\
                .cadastrar_item('iPad Mini 16GB','1234')\
                .verificar_mensagem_sucesso()\
                .verificar_diferenca_numero_itens(1)\
                .validar_ultimo_item()

    def teste_remocao_ultimo_produto(self):
        self.acoes_produto\
            .acessar_pagina()\
                .contar_itens()\
                .remover_ultimo_item()\
                .verificar_diferenca_numero_itens(-1)\

    @classmethod
    def tearDownClass(self):
        self.driver.quit()