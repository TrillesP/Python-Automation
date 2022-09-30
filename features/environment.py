from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome('drivers/chrome/106/chromedriver.exe')


def after_all(context):
    context.driver.quit()
