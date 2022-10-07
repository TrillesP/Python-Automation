@login
Feature: Login
  Scenario Outline: Login direto Negativo
    Given que acesso o site BlazeDemo
    When clicko em Home
    Then exibe pagina de login
    When preencho <email> e <senha>
    And clicko em login
    Then verifico que registro não existe
    Examples:
      | email                    | senha          |
      | "abacaxi@banana.morango" | "123456"       |
      | "carambola@abacate.mama" | "464538"       |

  Scenario Outline: Registro Positivo
    Given que acesso o site BlazeDemo
    When clicko em Home
    Then exibe pagina de login
    When clicko em registrar
    Then exibe pagina de registro
    When preencho <name> <company> <email> e <password>
    And clicko em registro
    Then verifico que login foi feito
    Examples:
    | name                 | company            | email                        | password        |
    | "teste109"            | "casa"             | "abacaxi@banana.morango7"    | "535689"        |