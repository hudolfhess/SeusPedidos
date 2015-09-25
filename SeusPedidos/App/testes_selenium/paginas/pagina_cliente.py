from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from SeusPedidos.App.testes_selenium.paginas.pagina_base import PaginaBase

__author__ = 'hcassus'

class PaginaCliente(PaginaBase):

    locator_nome = (By.ID,'clienteNome')
    locator_email = (By.ID,'clienteEmail')
    locator_salvar = (By.XPATH,'//input[@value="Editar cliente"]')
    locator_adicionar = (By.XPATH,'//input[@value="Adicionar"]')
    locator_alerta = (By.XPATH, '//div[contains(@class,"alert")]')
    xpath_clientes = '//tr[@ng-repeat="cliente in clientes"]'
    xpath_ultimo_cliente = xpath_clientes + '[last()]'
    locator_nome_ultimo_cliente = (By.XPATH, xpath_ultimo_cliente + '/td[1]')
    locator_email_ultimo_cliente = (By.XPATH, xpath_ultimo_cliente + '/td[2]')
    locator_remover_ultimo_cliente = (By.XPATH, xpath_ultimo_cliente + '/td[3]/button[text()="Remover"]')
    locator_editar_ultimo_cliente = (By.XPATH, xpath_ultimo_cliente + '/td[3]/button[text()="Editar"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)

    def contar_clientes(self):
        return len(self.obter_todos_elementos((By.XPATH, self.xpath_clientes)))

    def preencher_nome(self, nome):
        self.preencher_campo(PaginaCliente.locator_nome,nome)

    def preencher_email(self, valor):
        self.preencher_campo(PaginaCliente.locator_email,valor)

    def clicar_adicionar(self):
        self.clicar_elemento(self.locator_adicionar)

    def obter_texto_alerta(self):
        return self.obter_texto_elemento(self.locator_alerta)

    def obter_nome_ultimo_cliente(self):
        return self.obter_texto_elemento(self.locator_nome_ultimo_cliente)

    def obter_email_ultimo_cliente(self):
        return self.obter_texto_elemento(self.locator_email_ultimo_cliente)

    def remover_ultimo_cliente(self):
        self.remover_item(self.locator_remover_ultimo_cliente)

    def editar_ultimo_cliente(self):
        self.clicar_elemento(self.locator_editar_ultimo_cliente)

    def salvar_alteracoes(self):
        self.clicar_elemento(self.locator_salvar)
        self.wait.until(EC.presence_of_element_located(PaginaCliente.locator_adicionar))