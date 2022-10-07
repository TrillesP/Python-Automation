from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()

def after_all(context):
    context.driver.close()
