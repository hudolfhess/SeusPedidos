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

    def acessar(self):
        self.driver.get('http://localhost:8000/pedido')
        print self.live_server_url

    def contar_pedidos(self):
        return len(self.driver.find_elements(*PaginaListaPedidos.locator_todos_pedidos))

    def obter_cliente_ultimo_pedido(self):
        self.wait.until(EC.presence_of_element_located(PaginaListaPedidos.locator_cliente_ultimo_pedido))
        cliente_ultimo_pedido = self.driver.find_element(*PaginaListaPedidos.locator_cliente_ultimo_pedido)
        return cliente_ultimo_pedido.text


    def obter_status_ultimo_pedido(self):
        status_ultimo_pedido = self.driver.find_element(*PaginaListaPedidos.locator_status_ultimo_pedido)
        return status_ultimo_pedido.text

    def remover_ultimo_pedido(self):
        elemento_ultimo_pedido = self.driver.find_element(*PaginaListaPedidos.locator_remover_ultimo_pedido)
        elemento_ultimo_pedido.click()
        self.driver.switch_to_alert().accept()
        self.wait.until(EC.staleness_of(elemento_ultimo_pedido))

    def adicionar_pedido(self):
        elemento_adicionar_pedido = self.driver.find_element(*PaginaListaPedidos.locator_adicionar_pedido)
        elemento_adicionar_pedido.click()
        self.wait.until(EC.staleness_of(elemento_adicionar_pedido))
