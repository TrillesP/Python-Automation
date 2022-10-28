:fire: Para rodar o teste é necessário instalar as seguintes extensões do PyCharm, além do próprio programa instalado: <i>'selenium'</i>, <i>'webdriver-manager'</i>, <i>'behave'</i> e <i>'selenium-page-factory'</i>.

Para fazer isso, basta clicar na aba 'Python Packages', perto do 'Terminal' dentro do programa, pesquisar pelos nomes e instalar cada uma.

<h2>Testes de Automação do site BlazeDemo</h2>

:facepunch: Duas `features` são testadas, cada uma com vários cenários diferentes. Uma testa a procura passagens de avião e a devida compra, enquanto a outra testa o sistema de login do site e o de registro.

Como o site é montado justamente para experimentação o teste é feito apenas em front-end para verificar se aparece o esperado nas páginas carregadas, ou verifica como o site responde.

:facepunch: É utilizado `behave` para rodar as features do <b>Cucumber</b> em Python. Foi criado um arquivo de `environment` para especificar o driver a ser utilizado e fazer sua instalação (utilizando a extensão 'webdriver-manager' para PyCharm).

:facepunch: Para separar o mapeamento das páginas foram criados três arquivos de páginas (base_page.py, elementos.py e paginas.py) em `pages`. Uma conexão entre eles é feita pela importação de classes e pelo PageFactory. Arquivos vazios '__init__.py' foram criados em cada pasta para que os outros arquivos *.py fossem identificados como modules.

:facepunch: Na pasta `steps` se encontram as duas diferentes features a serem testadas com suas variáveis. Para verificar os logins e registros siga as instruções em comentário no próprio arquivo .feature.

:smile: Além disso há também um pequeno arquivo `evidencias.py` que serve para tirar screenshots de algumas páginas do site.

_________________________________

PS: como o site BlazeDemo é feito para experimentação, às vezes se encontra fora de ar e apresenta uma página não encontrada.
