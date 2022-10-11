from seleniumpagefactory import PageFactory

from features.pages import base_page


class TextBox(PageFactory, base_page.Base):
    def __init__(self, context):
        base_page.Base.__init__(
            self,
            context.driver)

    locators = {
        'nome': ('id', 'name'),
        'empresa': ('id', 'company'),
        'email': ('id', 'email'),
        'senha': ('id', 'password'),
        'senha_confirma': ('id', 'password-confirm'),
        'nome_completo': ('id', 'inputName'),
        'endereco': ('id', 'address'),
        'cidade': ('id', 'city'),
        'estado': ('id', 'state'),
        'cep': ('id', 'zipCode'),
        'cartao': ('id', 'creditCardNumber'),
        'cartao_mes': ('id', 'creditCardMonth'),
        'cartao_ano': ('id', 'creditCardYear'),
        'nome_cartao': ('id', 'nameOnCard'),
    }

    def preenche_nome(self, valor):
        self.nome.set_text(valor)

    def preenche_empresa(self, valor):
        self.empresa.set_text(valor)

    def preenche_email(self, valor):
        self.email.set_text(valor)

    def preenche_senha(self, valor):
        self.senha.set_text(valor)

    def preenche_senha_confirma(self, valor):
        self.senha_confirma.set_text(valor)

    def preenche_nome_completo(self, valor):
        self.nome_completo.set_text(valor)

    def preenche_endereco(self, valor):
        self.endereco.set_text(valor)

    def preenche_cidade(self, valor):
        self.cidade.set_text(valor)

    def preenche_estado(self, valor):
        self.estado.set_text(valor)

    def preenche_cep(self, valor):
        self.cep.set_text(valor)

    def preenche_cartao(self, valor):
        self.cartao.set_text(valor)

    def preenche_cartao_mes(self, valor):
        self.cartao_mes.set_text(valor)

    def preenche_cartao_ano(self, valor):
        self.cartao_ano.set_text(valor)

    def preenche_nome_cartao(self, valor):
        self.nome_cartao.set_text(valor)