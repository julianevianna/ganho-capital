# **Code Challange: Ganho de Capital**

## **Contexto**
Exercício com o objetivo de implementar um programa de linha de comando que calcula o imposto a ser pago sobre lucros ou prejuízos de operações no mercado financiero de ações.

## **Regras e Critérios de Aceite**

### **JOB STORY**
**Como** um usuário da CLI

**Eu quero** incluir uma lista de operações do mercado financeiro

**Para que** eu receba as informações de imposto a serem pagas para cada operação

### **CT01 - Imposto sobre operação de compra**
**Dado** um usuário incluíndo operações

**Quando** for uma operação de compra

**Então** não haverá imposto sobre a operação

### **CT02 - Atualização de preço médio ponderado**
**Dado** um usuário incluíndo operações

**Quando** for uma operação de compra

**Então** O preço médio ponderado de compra deverá ser atualizado

### **CT03 - Imposto sobre operação de venda**
**Dado** um usuário incluíndo uma operação de venda

**Quando** o valor da operação for maior que R$20.000,00 reais **E** for uma operação que gerou lucro

**Então** existirá cobrança de 20% de imposto sobre o lucro da operação

### **CT04 - Prejuízo**
**Dado** um usuário incluíndo uma operação de venda

**Quando** a operação resultar em prejuízo

**Então** o prejuízo deverá ser subtraido dos lucros das operações seguintes, até que ele seja deduzido por completo


### **CT05 - Lucro X Prejuízo**
**Dado** um usuário incluíndo uma operação de venda

**Quando** a operação resultar em lucro após uma operação que resultou prejuízo

**Então** o prejuízo deverá ser subtraido do lucro obtido **E** se o resultado ainda for positivo o imposto de 20% deve ser aplicado **OU** se o resultado for zero o imposto será zero **OU** se o resultado for negativo o imposto será zero e o resto do prejuízo será subtraído da próxima operação com lucro


### **CT06 - Entrada X Saída**
**Dado** um usuário incluíndo lista de operações

**Quando** uma entrada tiver o formato JSON, contendo os valores de operation(Tipo da operação (buy, sell)), unit-cost(Preço unitário da ação) e quantity(Quantidade de ações negociadas)

**Então** sua saída deverá ser uma lista em formato JSON, contento o valor tax(Valor do imposto pago em uma operação)

### **CT06 - Arredondamento de casas decimais**
**Dado** um valor em moeda

**Quando** tiver algum valor quebrado

**Então** ele deverá ser arredondado com duas casas decimais