from behave import *
from features.pages import paginas, elementos


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
    context.elemento = elementos.TextBox(context)
    context.elemento.preenche_nome_completo(nome)
    context.elemento.preenche_endereco(endereco)
    context.elemento.preenche_cidade(cidade)
    context.elemento.preenche_estado(estado)
    context.elemento.preenche_cep(cep)
    context.elemento.preenche_cartao(numeroCart)
    context.elemento.preenche_cartao_mes(mesCart)
    context.elemento.preenche_cartao_ano(anoCart)
    context.elemento.preenche_nome_cartao(nomeCart)
    context.pagina_home = paginas.Home(context)
    context.pagina_home.click_search()


@then(u'valido se a passagem foi comprada')
def valido_se_a_passagem_foi_comprada(context):
    context.pagina_home = paginas.Home(context)
    assert context.pagina_home.compra_check() is True