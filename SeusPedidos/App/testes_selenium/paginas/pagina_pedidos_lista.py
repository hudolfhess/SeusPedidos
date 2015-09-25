from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from SeusPedidos.App.testes_selenium.paginas.pagina_base import PaginaBase

__author__ = 'hcassus'

class PaginaListaPedidos(PaginaBase):

    locator_cliente_ultimo_pedido = (By.XPATH, '//tr[@ng-repeat="_pedido in pedidos"][last()]/td[2]')
    locator_status_ultimo_pedido = (By.XPATH, '//tr[@ng-repeat="_pedido in pedidos"][last()]/td[4]')
    locator_adicionar_pedido = (By.XPATH, '//a[text()="Adicionar pedido"]')
    locator_remover_ultimo_pedido = (By.XPATH, '//tr[@ng-repeat="_pedido in pedidos"][last()]/td[6]/button[text()="Remover"]')
    locator_todos_pedidos = (By.XPATH,'//tr[@ng-repeat="_pedido in pedidos"]')


    def contar_pedidos(self):
        return len(self.obter_todos_elementos(self.locator_todos_pedidos))

    def obter_cliente_ultimo_pedido(self):
        self.wait.until(EC.presence_of_element_located(self.locator_cliente_ultimo_pedido))
        return self.obter_texto_elemento(self.locator_cliente_ultimo_pedido)


    def obter_status_ultimo_pedido(self):
        return self.obter_texto_elemento(self.locator_status_ultimo_pedido)

    def remover_ultimo_pedido(self):
        self.remover_item(self.locator_remover_ultimo_pedido)

    def adicionar_pedido(self):
        elemento_adicionar_pedido = self.driver.find_element(*self.locator_adicionar_pedido)
        self.clicar_elemento(self.locator_adicionar_pedido)
        self.wait.until(EC.staleness_of(elemento_adicionar_pedido))
