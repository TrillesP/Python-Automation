import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestConsultaCurso():

    def setup_method(self):
        self.driver = webdriver.Chrome('drivers/chrome/100/chromedriver.exe')
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_procurar_curso(self):
        delay = 3
        wait = WebDriverWait(self.driver, delay)
        self.driver.get("https://iterasys.com.br/pt/cursos")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))
        self.driver.find_element(By.ID, "auto-2").click()
        self.driver.find_element(By.ID, "auto-2").send_keys("Python")
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h3"), "Python"))
        self.driver.find_element(By.CSS_SELECTOR, "h3").click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h1"), "Python"))
        assert "Python" in self.driver.title
        assert self.driver.find_element(By.CSS_SELECTOR, "div.content-price").text == "R$ 0,00"
