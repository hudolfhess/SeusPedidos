from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'hcassus'

class PaginaBase:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def obter_elemento(self, **locator):
        return self.driver.find_element(locator)

    def obter_titulo(self):
        return self.driver.title

    def acessar_url(self,url):
        self.driver.get(url)