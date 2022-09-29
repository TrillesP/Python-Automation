from behave import *

def before_feature(context,feature):
    if 'compra_passagem' in feature.tag:
        context.execute_steps(

        )

@given('que acesso o site BlazeDemo')
def que_acesso_o_site_BlazeDemo(context):
    print('Passo 1 - Abriu site.')
    ...

@when('pesquiso passagens de "{origem}" a "{destino}"')
def pesquiso_passagens_de_sao_paulo_a_new_york(context,origem,destino):
    print('Passo 2 - Pesquisou.')
    ...

@when('seleciono o primeiro voo')
def seleciono_o_primeiro_voo(context):
    print('Passo 3 - Selecionou primeiro voo.')
    ...

@when('preencho os dados de pagamento')
def preencho_os_dados_de_pagamento(context):
    print('Passo 4 - Preencheu dados.')
    ...

@then('valido se a passagem foi comprada')
def valido_se_a_passagem_foi_comprada(context):
    print('Passo 5 - Validou compra.')
    ...

