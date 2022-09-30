import os
import time
from datetime import datetime

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

caminho_print = '../prints/' + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '/'


def testar_blazedemo():
    os.makedirs(caminho_print)
    driver = webdriver.Chrome(executable_path='../drivers/chrome/106/chromedriver.exe')
    driver.get("https://blazedemo.com")
    time.sleep(5)
    driver.get_screenshot_as_file(f'{caminho_print}home.png')
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()
    time.sleep(5)
    driver.get_screenshot_as_file(f'{caminho_print}voos.png')
    time.sleep(3)
    driver.quit()
