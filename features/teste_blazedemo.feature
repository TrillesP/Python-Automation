@compra_passagem
Feature: Compra de Passagem Aerea
  Scenario: Viagem de Sao Paulo a New York
    Given que acesso o site BlazeDemo
    When pesquiso passagens de "São Paolo" a "New York"
    And seleciono o primeiro voo
    And preencho os dados de pagamento
    Then valido se a passagem foi comprada

  Scenario: Viagem de Paris a Dublin
    Given que acesso o site BlazeDemo
    When pesquiso passagens de "Paris" a "Dublin"
    And seleciono o primeiro voo
    And preencho os dados de pagamento
    Then valido se a passagem foi comprada
