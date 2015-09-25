from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from SeusPedidos.App.testes_selenium.paginas.pagina_base import PaginaBase
from selenium.webdriver.support import expected_conditions as EC

__author__ = 'hcassus'

class PaginaEdicaoPedidos(PaginaBase):

    locator_clientes = (By.ID,'listaClientes')
    locator_produtos = (By.ID,'listaProdutos')
    locator_adicionar_item = (By.XPATH,'//input[@value="Adicionar produto"]')
    locator_gerar_pedido = (By.XPATH,'//input[@value="Gerar pedido"]')
    locator_alerta = (By.XPATH, '//div[contains(@class,"alert")]')
    locator_quantidade  = (By.ID,'inputQuantidade')
    locator_desconto = (By.ID,'inputDesconto')


    def adicionarPedido(self):
        self.clicar_elemento(self.locator_gerar_pedido)


    def selecionarCliente(self, cliente):
        self.selecionar_combo(self.locator_clientes,cliente)

    def adicionarItem(self, item, quantidade, desconto):
        self.selecionar_combo(self.locator_produtos,item)
        self.preencher_campo(self.locator_quantidade,quantidade)
        self.preencher_campo(self.locator_desconto,desconto)
        self.clicar_elemento(self.locator_adicionar_item)




