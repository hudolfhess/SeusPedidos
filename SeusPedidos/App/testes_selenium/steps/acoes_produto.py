from SeusPedidos.App.testes_selenium.paginas.pagina_produto import PaginaProduto
from SeusPedidos.App.testes_selenium.steps.acoes_base import AcoesBase

__author__ = 'hcassus'

class AcoesProduto(AcoesBase):

    def __init__(self, driver):
        self.pagina = PaginaProduto(driver)

    def cadastrar_item(self,nome,valor):
        self.alterar_nome(nome)
        self.alterar_valor(valor)
        self.pagina.clicar_adicionar()
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

    def editar_ultimo_item(self,nome,valor):
        self.pagina.editar_ultimo_produto()
        self.alterar_nome(nome)
        self.alterar_valor(valor)
        self.pagina.clicar_salvar_alteracoes()
        return self

    def alterar_nome(self,nome):
        self.pagina.preencher_nome(nome)
        self.nome_produto = nome
        return self

    def alterar_valor(self,valor):
        self.pagina.preencher_valor(valor)
        self.valor_produto = valor
        return self

