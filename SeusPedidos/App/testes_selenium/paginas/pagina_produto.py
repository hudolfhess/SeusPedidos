from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from SeusPedidos.App.testes_selenium.paginas.pagina_base import PaginaBase

__author__ = 'hcassus'

class PaginaProduto(PaginaBase):

    locator_nome = (By.ID,'produtoNome')
    locator_valor = (By.ID,'produtoValor')
    locator_adicionar = (By.XPATH,'//input[@value="Adicionar"]')
    locator_salvar_alteracoes = (By.XPATH,'//input[@value="Editar produto"]')
    locator_alerta = (By.XPATH, '//div[contains(@class,"alert")]')
    xpath_clientes = '//tr[@ng-repeat="produto in produtos"]'
    xpath_ultimo_cliente = xpath_clientes + '[last()]'
    locator_nome_ultimo_produto = (By.XPATH, xpath_ultimo_cliente + '/td[1]')
    locator_valor_ultimo_produto = (By.XPATH, xpath_ultimo_cliente + '/td[2]')
    locator_remover_ultimo_produto = (By.XPATH, xpath_ultimo_cliente + '/td[3]/button[text()="Remover"]')
    locator_editar_ultimo_produto = (By.XPATH, xpath_ultimo_cliente + '/td[3]/button[text()="Editar"]')

    def contar_itens(self):
        return len(self.obter_todos_elementos((By.XPATH, self.xpath_clientes)))

    def preencher_nome(self, nome):
        self.preencher_campo(self.locator_nome,nome)

    def preencher_valor(self, valor):
        self.preencher_campo(self.locator_valor, valor)

    def clicar_adicionar(self):
        self.clicar_elemento(self.locator_adicionar)

    def obter_texto_alerta(self):
        return self.obter_texto_elemento(self.locator_alerta)

    def obter_nome_ultimo_produto(self):
        return self.obter_texto_elemento(self.locator_nome_ultimo_produto)

    def obter_valor_ultimo_produto(self):
        return self.obter_texto_elemento(self.locator_valor_ultimo_produto)

    def remover_ultimo_produto(self):
        self.remover_item(self.locator_remover_ultimo_produto)

    def editar_ultimo_produto(self):
        self.clicar_elemento(self.locator_editar_ultimo_produto)

    def clicar_salvar_alteracoes(self):
        self.clicar_elemento(self.locator_salvar_alteracoes)
        self.wait.until(EC.presence_of_element_located(self.locator_adicionar))