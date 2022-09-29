@compra_passagem

Feature: Compra de Passagem Aerea
  Scenario: Viagem de Sao Paulo a New York
    Given que acesso o site BlazeDemo
    When pesquiso passagens de "Sao Paulo" a "New York"
    And seleciono o primeiro voo
    And preencho os dados de pagamento
    Then valido se a passagem foi comprada

Feature: Compra de Passagem Aerea
  Scenario: Viagem de NewYork a Dublin
    Given que acesso o site BlazeDemo
    When pesquiso passagens de "New York" a "Dublin"
    And seleciono o primeiro voo
    And preencho os dados de pagamento
    Then valido se a passagem foi comprada
