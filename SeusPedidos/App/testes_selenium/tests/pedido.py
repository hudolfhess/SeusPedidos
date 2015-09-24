from django.core.management import call_command
from django_liveserver.testcases import LiveServerTestCase
from selenium import webdriver
from SeusPedidos.App.testes_selenium.steps.acoes_pedido import AcoesPedido

__author__ = 'hcassus'


class TestesPedido(LiveServerTestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.acoes_pedido = AcoesPedido(self.driver)
        call_command('flush',interactive=False, verbosity=0)
        call_command('loaddata', 'base.json', verbosity=0)

        super(TestesPedido, self).setUp()

    def teste_cadastro_pedido_valido(self):
        self.acoes_pedido\
            .acessar_pagina(self.live_server_url+'/pedido')\
                .contar_pedidos()\
                .cadastrar_pedido('Hudolf Hess', [('iPad Air 2',10,5),('Mac Book 256GB Intel Core M',10,0)])\
                .verificar_diferenca_numero_pedidos(1)\
                .validar_ultimo_pedido()

    def teste_remocao_ultimo_produto(self):
        self.acoes_pedido\
            .acessar_pagina(self.live_server_url+'/pedido')\
                .contar_pedidos()\
                .remover_ultimo_pedido()\
                .verificar_diferenca_numero_pedidos(-1)

    def tearDown(self):
        self.driver.quit()
        super(TestesPedido, self).tearDown()