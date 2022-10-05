@compra_passagem
Feature: Compra de Passagem Aerea
  Scenario Outline: Viagem de Sao Paulo a New York
    Given que acesso o site BlazeDemo
    When pesquiso passagens de <origem> a <destino>
    And seleciono o primeiro voo
    And preencho os dados de pagamento
    Then valido se a passagem foi comprada
    Examples:
    | origem      | destino    |
    | "São Paolo" | "New York" |
    | "Boston"    | "Dublin"   |
    | "Paris"     | "Rome"     |