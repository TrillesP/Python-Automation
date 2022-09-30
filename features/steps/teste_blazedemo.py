from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def before_feature(context, feature):
    if 'compra_passagem' in feature.tag:
        context.execute_steps(

        )


@given('que acesso o site BlazeDemo')
def que_acesso_o_site_BlazeDemo(context):
    context.driver.get("https://blazedemo.com")
    print('Passo 1 - Abriu site.')


@when('pesquiso passagens de "{origem}" a "{destino}"')
def pesquiso_passagens_de_sao_paulo_a_new_york(context, origem, destino):
    elemento_origem = context.driver.find_element(By.NAME, 'fromPort')
    objeto_origem = Select(elemento_origem)
    objeto_origem.select_by_visible_text(origem)
    elemento_destino = context.driver.find_element(By.NAME, 'toPort')
    objeto_destino = Select(elemento_destino)
    objeto_destino.select_by_visible_text(destino)
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()
    print('Passo 2 - Pesquisou.')


@when('seleciono o primeiro voo')
def seleciono_o_primeiro_voo(context):
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-small').click()
    print('Passo 3 - Selecionou primeiro voo.')


@when('preencho os dados de pagamento')
def preencho_os_dados_de_pagamento(context):
    context.driver.find_element(By.ID, 'inputName').send_keys('Pedro Trilles')
    context.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()
    print('Passo 4 - Preencheu dados.')


@then('valido se a passagem foi comprada')
def valido_se_a_passagem_foi_comprada(context):
    assert context.driver.title == 'BlazeDemo Confirmation'
    print('Passo 5 - Validou compra.')
