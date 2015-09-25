from django.core.management import call_command
from django_liveserver.testcases import LiveServerTestCase
from selenium import webdriver
from SeusPedidos.App.testes_selenium.steps.acoes_produto import AcoesProduto

__author__ = 'hcassus'


class TestesProduto(LiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.acoes_produto = AcoesProduto(self.driver)
        call_command('flush', verbosity=0, interactive=False)
        call_command('loaddata', 'base.json', verbosity=0)
        self.url_pagina = self.live_server_url+'/produto'

        super(TestesProduto, self).setUp()

    def teste_cadastro_produto_valido(self):
        self.acoes_produto\
            .acessar_pagina(self.url_pagina)\
                .contar_itens()\
                .cadastrar_item('iPad Mini 16GB','1234')\
                .verificar_mensagem_sucesso()\
                .verificar_diferenca_numero_itens(1)\
                .validar_ultimo_item()

    def teste_remocao_ultimo_produto(self):
        self.acoes_produto\
            .acessar_pagina(self.url_pagina)\
                .contar_itens()\
                .remover_ultimo_item()\
                .verificar_diferenca_numero_itens(-1)\

    def teste_edicao_ultimo_produto(self):
        self.acoes_produto\
            .acessar_pagina(self.url_pagina)\
                .contar_itens()\
                .editar_ultimo_item('iPad Mini 2','3500')\
                .verificar_diferenca_numero_itens(0)\
                .validar_ultimo_item()

    def tearDown(self):
        self.driver.quit()
        super(TestesProduto, self).tearDown()