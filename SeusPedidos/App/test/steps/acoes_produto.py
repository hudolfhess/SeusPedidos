from time import sleep
from SeusPedidos.App.test.paginas.pagina_produto import PaginaProduto

__author__ = 'hcassus'

class AcoesProduto:

    def __init__(self, driver):
        self.pagina = PaginaProduto(driver)

    def acessar_pagina(self):
        self.pagina.acessar()
        return self

    def cadastrar_item(self,nome,valor):
        self.pagina.preencher_nome(nome)
        self.pagina.preencher_valor(valor)
        self.pagina.clicar_adicionar()

        self.nome_produto = nome
        self.valor_produto = valor
        return self

    def contar_itens(self):
        self.contagem = self.pagina.contar_itens()
        return self

    def verificar_mensagem_sucesso(self):
        assert 'Dados salvos com sucesso!' in self.pagina.obter_texto_alerta()
        return self

    def verificar_diferenca_numero_itens(self,numero):
        assert self.pagina.contar_itens() == self.contagem + numero
        return self

    def validar_ultimo_item(self):
        assert self.nome_produto == self.pagina.obter_nome_ultimo_produto()
        assert self.valor_produto == self.pagina.obter_valor_ultimo_produto()
        return self

    def remover_ultimo_item(self):
        self.pagina.remover_ultimo_produto()
        return self