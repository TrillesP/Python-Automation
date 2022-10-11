from features.pages import paginas, elementos
from behave import *


def before_feature(context, feature):
    if 'login' in feature.tag:
        context.execute_steps(

        )


@given('que acesso o site BlazeDemo')
def step_impl(context):
    context.pagina_home = paginas.Home(context)
    context.pagina_home.visit('https://blazedemo.com')
    assert context.pagina_home.title_check() is True


@when(u'clicko em Home')
def step_impl(context):
    context.pagina_home.click_home()


@then(u'exibe pagina de login')
def step_impl(context):
    context.pagina_home = paginas.LoginReg(context)
    assert context.pagina_home.login_page_check() is True


@when(u'clicko em registrar')
def step_impl(context):
    context.pagina_home = paginas.Home(context)
    context.pagina_home.click_register()

@then(u'exibe pagina de registro')
def step_impl(context):
    context.pagina_home = paginas.LoginReg(context)
    assert context.pagina_home.registro_page_check() is True


@when(u'preencho "{name}" "{company}" "{email}" e "{password}"')
def step_impl(context, name, company, email, password):
    context.elemento = elementos.TextBox(context)
    context.elemento.preenche_nome(name)
    context.elemento.preenche_empresa(company)
    context.elemento.preenche_email(email)
    context.elemento.preenche_senha(password)
    context.elemento.preenche_senha_confirma(password)


@when(u'preencho "{email}" e "{senha}"')
def step_impl(context, email, senha):
    context.elemento = elementos.TextBox(context)
    context.elemento.preenche_email(email)
    context.elemento.preenche_senha(senha)

@when(u'clicko em registro')
def step_impl(context):
    context.pagina_home = paginas.Home(context)
    context.pagina_home.click_LR()


@when(u'clicko em login')
def step_impl(context):
    context.pagina_home = paginas.Home(context)
    context.pagina_home.click_LR()


@then(u'verifico que login foi feito')
def step_impl(context):
    context.pagina_home = paginas.LoginReg(context)
    assert context.pagina_home.login_done_check() is True


@then(u'verifico que registro não existe')
def step_impl(context):
    context.pagina_home = paginas.LoginReg(context)
    assert context.pagina_home.registro_nao_existente() is True
