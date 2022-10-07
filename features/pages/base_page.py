from selenium.webdriver.common.by import By

class Base(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def visit(self, url):
        self.driver.get(url)

    def click_search(self):
        botao = self.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary')
        botao.click()

    def click_home(self):
        botao = self.driver.find_element(By.LINK_TEXT, 'home')
        botao.click()

    def click_register(self):
        botao = self.driver.find_element(By.LINK_TEXT, 'Register')
        botao.click()

    def click_LR(self):
        botao = self.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
        botao.click()