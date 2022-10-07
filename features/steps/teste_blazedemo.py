from behave import *
from features.pages import paginas


def before_feature(context, feature):
    if 'compra_passagem' in feature.tag:
        context.execute_steps(

        )


@when(u'pesquiso passagens de "{origem}" a "{destino}"')
def pesquiso_passagens_de_sao_paulo_a_new_york(context, origem, destino):
    context.pagina_home = paginas.Home(context)
    context.pagina_home.seleciona_origem(origem)
    context.pagina_home.seleciona_destino(destino)
    context.pagina_home.click_search()


@when(u'seleciono o primeiro voo')
def seleciono_o_primeiro_voo(context):
    context.pagina_home = paginas.Voos(context)
    context.pagina_home.selecionar_primeiro()


@when(u'preencho os dados de pagamento, com "{nome}", "{endereco}", "{cidade}", "{estado}", "{cep}",'
      u' "{numeroCart}", "{mesCart}", "{anoCart}", "{nomeCart}" e efetuo compra')
def preencho_os_dados_de_pagamento(context, nome, endereco, cidade, estado, cep, numeroCart, mesCart, anoCart, nomeCart):
    context.pagina_home = paginas.Voos(context)
    context.pagina_home.preenche_NOMECOMP = nome
    context.pagina_home.preenche_END = endereco
    context.pagina_home.preenche_CIDADE = cidade
    context.pagina_home.preenche_ESTADO = estado
    context.pagina_home.preenche_CEP = cep
    context.pagina_home.preenche_CARTAO = numeroCart
    context.pagina_home.preenche_MES = mesCart
    context.pagina_home.preenche_ANO = anoCart
    context.pagina_home.preenche_NOMECART = nomeCart
    context.pagina_home = paginas.Home(context)
    context.pagina_home.click_search()


@then(u'valido se a passagem foi comprada')
def valido_se_a_passagem_foi_comprada(context):
    context.pagina_home = paginas.Home(context)
    assert context.pagina_home.compra_check() is True