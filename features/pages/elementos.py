from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CaixaID(object):
    def __set__(context, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.ID, context.box))
        driver.find_element(By.ID, context.box).clear()
        driver.find_element(By.ID, context.box).send_keys(value)