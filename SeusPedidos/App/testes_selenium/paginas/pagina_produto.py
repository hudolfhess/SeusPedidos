from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from SeusPedidos.App.testes_selenium.paginas.pagina_base import PaginaBase

__author__ = 'hcassus'

class PaginaProduto(PaginaBase):

    locator_nome = (By.ID,'produtoNome')
    locator_valor = (By.ID,'produtoValor')
    locator_adicionar = (By.XPATH,'//input[@value="Adicionar"]')
    locator_alerta = (By.XPATH, '//div[contains(@class,"alert")]')
    locator_nome_ultimo_produto = (By.XPATH, '//tr[@ng-repeat="produto in produtos"][last()]/td[1]')
    locator_valor_ultimo_produto = (By.XPATH, '//tr[@ng-repeat="produto in produtos"][last()]/td[2]')
    locator_remover_ultimo_produto = (By.XPATH, '//tr[@ng-repeat="produto in produtos"][last()]/td[3]/button[text()="Remover"]')


    def acessar(self):
        self.driver.get('http://localhost:8000/produto')
        print self.live_server_url

    def contar_itens(self):
        return len(self.driver.find_elements(By.XPATH,'//tr[@ng-repeat="produto in produtos"]'))

    def preencher_nome(self, nome):
        campo_nome = self.driver.find_element(*PaginaProduto.locator_nome)
        campo_nome.send_keys(nome)

    def preencher_valor(self, valor):
        campo_valor = self.driver.find_element(*PaginaProduto.locator_valor)
        campo_valor.send_keys(valor)

    def clicar_adicionar(self):
        botao_adicionar = self.driver.find_element(*PaginaProduto.locator_adicionar)
        botao_adicionar.click()

    def obter_texto_alerta(self):
        caixa_alerta = self.driver.find_element(*PaginaProduto.locator_alerta)
        return caixa_alerta.text

    def obter_nome_ultimo_produto(self):
        nome_ultimo_produto = self.driver.find_element(*PaginaProduto.locator_nome_ultimo_produto)
        return nome_ultimo_produto.text


    def obter_valor_ultimo_produto(self):
        valor_ultimo_produto = self.driver.find_element(*PaginaProduto.locator_valor_ultimo_produto)
        return valor_ultimo_produto.text

    def remover_ultimo_produto(self):
        elemento_remover_ultimo_produto = self.driver.find_element(*PaginaProduto.locator_remover_ultimo_produto)
        elemento_remover_ultimo_produto.click()
        self.driver.switch_to_alert().accept()
        self.wait.until(EC.staleness_of(elemento_remover_ultimo_produto))