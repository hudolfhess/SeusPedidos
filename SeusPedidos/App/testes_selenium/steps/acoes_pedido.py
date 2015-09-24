
from SeusPedidos.App.testes_selenium.paginas.pagina_pedidos_edicao import PaginaEdicaoPedidos
from SeusPedidos.App.testes_selenium.paginas.pagina_pedidos_lista import PaginaListaPedidos

__author__ = 'hcassus'


class AcoesPedido:

    def __init__(self, driver):
        self.paginaLista = PaginaListaPedidos(driver)
        self.paginaEdicao = PaginaEdicaoPedidos(driver)

    def acessar_pagina(self,url):
        #self.pagina.acessar()
        self.paginaLista.acessar_url(url)
        return self

    def contar_pedidos(self):
        self.contagem = self.paginaLista.contar_pedidos()
        return self

    def cadastrar_pedido(self, cliente, lista_produtos):
        self.paginaLista.adicionar_pedido()
        self.paginaEdicao.selecionarCliente(cliente)
        self.cliente = cliente
        for item in lista_produtos:
            nome_item = item[0]
            quantidade_item = item[1]
            desconto_item = item[2]
            self.paginaEdicao.adicionarItem(nome_item, quantidade_item, desconto_item)
        self.paginaEdicao.adicionarPedido()
        return self

    def verificar_diferenca_numero_pedidos(self, numero):
        assert self.paginaLista.contar_pedidos() == self.contagem + numero
        return self

    def validar_ultimo_pedido(self):
        assert self.cliente == self.paginaLista.obter_cliente_ultimo_pedido()
        assert 'Em aberto' == self.paginaLista.obter_status_ultimo_pedido()
        return self

    def remover_ultimo_pedido(self):
        self.paginaLista.remover_ultimo_pedido()
        return self
