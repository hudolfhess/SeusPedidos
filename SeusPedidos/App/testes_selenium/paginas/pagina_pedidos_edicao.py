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
        botao_adicionar = self.driver.find_element(*PaginaEdicaoPedidos.locator_gerar_pedido)
        botao_adicionar.click()


    def selecionarCliente(self, cliente):
        select_cliente =  Select(self.driver.find_element(*PaginaEdicaoPedidos.locator_clientes))
        select_cliente.select_by_visible_text(cliente)

    def adicionarItem(self, item, quantidade, desconto):
        select_produto =  Select(self.driver.find_element(*PaginaEdicaoPedidos.locator_produtos))
        campo_quantidade = self.driver.find_element(*PaginaEdicaoPedidos.locator_quantidade)
        campo_desconto = self.driver.find_element(*PaginaEdicaoPedidos.locator_desconto)
        botao_adicionar = self.driver.find_element(*PaginaEdicaoPedidos.locator_adicionar_item)

        select_produto.select_by_visible_text(item)
        campo_quantidade.send_keys(quantidade)
        campo_desconto.send_keys(desconto)
        botao_adicionar.click()




