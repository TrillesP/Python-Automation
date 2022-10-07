from selenium.webdriver.support.wait import WebDriverWait

from helpers.helper_base import Helper_Func


def __init__(context, driver):
    super(Helper_Func, context).__init__()
    context._driver_wait = WebDriverWait(driver, Helper_Func.__TIMEOUT)
    context._driver = driver

def open(self, url):
    self._driver.get(url)