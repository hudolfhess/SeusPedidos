from django_liveserver.testcases import LiveServerTestCase
from selenium import webdriver
from SeusPedidos.App.testes_selenium.steps.acoes_cliente import AcoesCliente
from django.core.management import call_command

__author__ = 'hcassus'


class TestesCliente(LiveServerTestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.acoes_cliente = AcoesCliente(self.driver)
        call_command('flush',interactive=False, verbosity=0)
        call_command('loaddata', 'base.json', verbosity=0)
        self.url_pagina = self.live_server_url+'/cliente'
        super(TestesCliente, self).setUp()

    def teste_cadastro_cliente_valido(self):
        self.acoes_cliente\
            .acessar_pagina(self.url_pagina)\
                .contar_clientes()\
                .cadastrar_cliente('Henrique Cassus','henrique.cassus@meuspedidos.com.br')\
                .verificar_mensagem_sucesso()\
                .verificar_diferenca_numero_clientes(1)\
                .validar_ultimo_cliente()

    def teste_remocao_ultimo_cliente(self):
        self.acoes_cliente\
            .acessar_pagina(self.url_pagina)\
                .contar_clientes()\
                .remover_ultimo_cliente()\
                .verificar_diferenca_numero_clientes(-1)\

    def teste_edicao_ultimo_cliente(self):
        self.acoes_cliente\
            .acessar_pagina(self.url_pagina)\
                .contar_clientes()\
                .editar_ultimo_cliente('Hudolf Hess','hhess@meuspedidos.com.br')\
                .verificar_diferenca_numero_clientes(0)\
                .validar_ultimo_cliente()


    def tearDown(self):
        self.driver.quit()
        super(TestesCliente, self).tearDown()