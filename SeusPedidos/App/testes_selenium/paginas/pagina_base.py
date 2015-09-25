from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'hcassus'

class PaginaBase:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)

    def obter_elemento(self, locator):
        return self.driver.find_element(*locator)

    def obter_todos_elementos(self, locator):
        return self.driver.find_elements(*locator)

    def acessar_url(self,url):
        self.driver.get(url)

    def preencher_campo(self, locator, valor):
        elemento = self.obter_elemento(locator)
        elemento.clear()
        elemento.send_keys(valor)

    def obter_texto_elemento(self,locator):
        return self.obter_elemento(locator).text

    def remover_item(self, locator_botao_remover):
        elemento_remover_item = self.obter_elemento(locator_botao_remover)
        elemento_remover_item.click()
        self.driver.switch_to_alert().accept()
        self.wait.until(EC.staleness_of(elemento_remover_item))

    def clicar_elemento(self, locator):
        elemento = self.obter_elemento(locator)
        elemento.click()

    def selecionar_combo(self,locator,valor):
        select =  Select(self.obter_elemento(locator))
        select.select_by_visible_text(valor)