from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from features.pages import base_page


class Home(base_page.Base):
    def __init__(self, context):
        base_page.Base.__init__(
            self,
            context.driver)

    def title_check(self):
        if "BlazeDemo" in self.driver.title:
            return True

    def seleciona_origem(self, valor):
        elem = self.driver.find_element(By.NAME, 'fromPort')
        obj = Select(elem)
        return obj.select_by_visible_text(valor)

    def seleciona_destino(self, valor):
        elem = self.driver.find_element(By.NAME, 'toPort')
        obj = Select(elem)
        return obj.select_by_visible_text(valor)

    def compra_check(self):
        if self.driver.title == 'BlazeDemo Confirmation':
            return True

class LoginReg(base_page.Base):
    def __init__(self, context):
        base_page.Base.__init__(
            self,
            context.driver)

    def login_page_check(self):
        if self.driver.find_element(By.CSS_SELECTOR, 'div.panel-heading').text == "Login":
            return True

    def registro_page_check(self):
        if self.driver.find_element(By.CSS_SELECTOR, 'div.panel-heading').text == "Register":
            return True

    def login_done_check(self):
        if self.driver.find_element(By.CSS_SELECTOR, 'div.panel-heading').text == "Dashboard":
            return True

    def registro_nao_existente(self):
        if self.driver.find_element(By.CSS_SELECTOR, 'span.help-block').text == "These credentials do not match our records.":
            return True


class Voos(base_page.Base):
    def __init__(self, context):
        base_page.Base.__init__(
            self,
            context.driver)

    def selecionar_primeiro(self):
        botao = self.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-small')
        botao.click()