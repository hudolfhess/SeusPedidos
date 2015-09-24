
from SeusPedidos.App.testes_selenium.paginas.pagina_pedidos_edicao import PaginaEdicaoPedidos
from SeusPedidos.App.testes_selenium.paginas.pagina_pedidos_lista import PaginaListaPedidos
from SeusPedidos.App.testes_selenium.steps.acoes_base import AcoesBase

__author__ = 'hcassus'


class AcoesPedido(AcoesBase):

    def __init__(self, driver):
        self.pagina = PaginaListaPedidos(driver)
        self.paginaEdicao = PaginaEdicaoPedidos(driver)

    def contar_pedidos(self):
        self.contagem = self.pagina.contar_pedidos()
        return self

    def cadastrar_pedido(self, cliente, lista_produtos):
        self.pagina.adicionar_pedido()
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
        assert self.pagina.contar_pedidos() == self.contagem + numero
        return self

    def validar_ultimo_pedido(self):
        assert self.cliente == self.pagina.obter_cliente_ultimo_pedido()
        assert 'Em aberto' == self.pagina.obter_status_ultimo_pedido()
        return self

    def remover_ultimo_pedido(self):
        self.pagina.remover_ultimo_pedido()
        return self
