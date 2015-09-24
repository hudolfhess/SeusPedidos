from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from SeusPedidos.App.testes_selenium.paginas.pagina_base import PaginaBase

__author__ = 'hcassus'

class PaginaCliente(PaginaBase):

    locator_nome = (By.ID,'clienteNome')
    locator_email = (By.ID,'clienteEmail')
    locator_adicionar = (By.XPATH,'//input[@value="Adicionar"]')
    locator_alerta = (By.XPATH, '//div[contains(@class,"alert")]')
    locator_nome_ultimo_cliente = (By.XPATH, '//tr[@ng-repeat="cliente in clientes"][last()]/td[1]')
    locator_email_ultimo_cliente = (By.XPATH, '//tr[@ng-repeat="cliente in clientes"][last()]/td[2]')
    locator_remover_ultimo_cliente = (By.XPATH, '//tr[@ng-repeat="cliente in clientes"][last()]/td[3]/button[text()="Remover"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def acessar(self):
        self.driver.get('http://localhost:8000/cliente')
        print self.live_server_url

    def contar_clientes(self):
        return len(self.driver.find_elements(By.XPATH,'//tr[@ng-repeat="cliente in clientes"]'))

    def preencher_nome(self, nome):
        campo_nome = self.driver.find_element(*PaginaCliente.locator_nome)
        campo_nome.send_keys(nome)

    def preencher_email(self, valor):
        campo_valor = self.driver.find_element(*PaginaCliente.locator_email)
        campo_valor.send_keys(valor)

    def clicar_adicionar(self):
        botao_adicionar = self.driver.find_element(*PaginaCliente.locator_adicionar)
        botao_adicionar.click()

    def obter_texto_alerta(self):
        caixa_alerta = self.driver.find_element(*PaginaCliente.locator_alerta)
        return caixa_alerta.text

    def obter_nome_ultimo_cliente(self):
        nome_ultimo_produto = self.driver.find_element(*PaginaCliente.locator_nome_ultimo_cliente)
        return nome_ultimo_produto.text


    def obter_email_ultimo_cliente(self):
        valor_ultimo_produto = self.driver.find_element(*PaginaCliente.locator_email_ultimo_cliente)
        return valor_ultimo_produto.text

    def remover_ultimo_cliente(self):
        elemento_ultimo_cliente = self.driver.find_element(*PaginaCliente.locator_remover_ultimo_cliente)
        elemento_ultimo_cliente.click()
        self.driver.switch_to_alert().accept()
        self.wait.until(EC.staleness_of(elemento_ultimo_cliente))
