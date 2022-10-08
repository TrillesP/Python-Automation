@compra_passagem
Feature: Compra de Passagem Aerea
  Scenario Outline: Viagens
    Given que acesso o site BlazeDemo
    When pesquiso passagens de <origem> a <destino>
    And seleciono o primeiro voo
    And preencho os dados de pagamento, com <nome>, <endereco>, <cidade>, <estado>, <cep>, <numeroCart>, <mesCart>, <anoCart>, <nomeCart> e efetuo compra
    Then valido se a passagem foi comprada
    Examples:
    | origem      | destino    | nome              | endereco         | cidade   | estado | cep      | numeroCart         | mesCart | anoCart | nomeCart          |
    | "São Paolo" | "New York" | "Abacaxi Morango" | "Rua das frutas" | "Fruta"  | "FT"   | "12345"  | "5555666677778888" | "12"    | "2050"  | "Abacaxi Morango" |
    | "Boston"    | "Dublin"   | "Abacaxi Morango" | "Rua das frutas" | "Fruta"  | "FT"   | "12345"  | "5555666677778888" | "12"    | "2050"  | "Abacaxi Morango" |
    | "Paris"     | "Rome"     | "Abacaxi Morango" | "Rua das frutas" | "Fruta"  | "FT"   | "12345"  | "5555666677778888" | "12"    | "2050"  | "Abacaxi Morango" |