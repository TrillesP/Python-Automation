import time

from behave import *
from selenium.webdriver.common.by import By


def before_feature(context, feature):
    if 'login' in feature.tag:
        context.execute_steps(

        )

@when(u'clicko em Home')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'home').click()

@then(u'exibe pagina de login')
def step_impl(context):
    time.sleep(1)
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.panel-heading').text == 'Login'

@when(u'clicko em registrar')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, 'Register').click()

@when(u'preencho "{name}" "{company}" "{email}" e "{password}"')
def step_impl(context, name, company, email, password):
    time.sleep(1)
    context.driver.find_element(By.ID, 'name').send_keys(name)
    context.driver.find_element(By.ID, 'company').send_keys(company)
    context.driver.find_element(By.ID, 'email').send_keys(email)
    context.driver.find_element(By.ID, 'password').send_keys(password)
    context.driver.find_element(By.ID, 'password-confirm').send_keys(password)

@when(u'preencho "{email}" e "{senha}"')
def step_impl(context, email, senha):
    time.sleep(1)
    context.driver.find_element(By.ID, 'email').send_keys(email)
    context.driver.find_element(By.ID, 'password').send_keys(senha)

@when(u'clicko em registro')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()


@when(u'clicko em login')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()


@then(u'verifico que login foi feito')
def step_impl(context):
    time.sleep(1)
    assert context.driver.find_element(By.CSS_SELECTOR, 'div.panel-heading').text == 'Dashboard'

@then(u'verifico que registro não existe')
def step_impl(context):
    time.sleep(1)
    assert context.driver.find_element(By.CSS_SELECTOR, 'span.help-block').text == 'These credentials do not match our records.'