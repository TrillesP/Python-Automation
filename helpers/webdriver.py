from selenium.webdriver.support.wait import WebDriverWait

from helpers.helper_base import Helper_Func


def __init__(self, driver):
    super(Helper_Func, self).__init__()
    self._driver_wait = WebDriverWait(driver, Helper_Func.__TIMEOUT)
    self._driver = driver

def open(self, url):
    self._driver.get(url)