from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Helper_Func(object):
    __TIMEOUT = 10  # segundos

    #Espera explícita
    def __init__(self, driver):                                           # função de inicialização de classe
        super(Helper_Func, self).__init__()                               # estabelece que driver herda de Helper_Func
        self._driver_wait = WebDriverWait(driver, Helper_Func.__TIMEOUT)  # criação de um objeto pra controlar esperas
        self._driver = driver

    #Abertura de uma URL/acesso de site
    def open(self, url):
        self._driver.get(url)

    #Maximizar tela
    def maximize(self):
        self._driver.maximize_window()

    #Fechar browser
    def close(self):
        self._driver.quit()

    #Funções uteis pra selecionar elementos
    def find_by_id(self, id):
        return self._driver_wait.until(EC.visibility_of_element_located(By.ID, id))

    def find_by_name(self, name):
        return self._driver_wait.until(EC.visibility_of_element_located(By.NAME, name))

    def find_by_css(self, css):
        return self._driver_wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, css))

    def find_by_xpath(self, xpath):
        return self._driver_wait.until(EC.visibility_of_element_located(By.XPATH, xpath))