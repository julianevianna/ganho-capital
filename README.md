# **Code Challange: Ganho de Capital**

## **Contexto**
Exercício com o objetivo de implementar um programa de linha de comando que calcula o imposto a ser pago sobre lucros ou prejuízos de operações no mercado financiero de ações.
<br><br><br>

-------------------------------------------------------------------------------------------------------------------------------------------------------

## **Regras e Critérios de Aceite**
Iremos começar definindo as regras e critérios de aceite do nosso challange, baseado no documento de especificações recebidos. 

A seguir iremos usar uma metodologia chamada BDD(Behavior-Driven Development), que é baseada nos princípios do TDD, porém com um foco maior no comeportamento do sistema do que nos testes. 

Para a definição do nosso caso de uso, utilizaremos o User Story, que utiliza uma estrutura simples: **"Como"**, **"Eu quero"**, **"Para que"**, para descrever a quem, ação e o resultado.

Para a definição dos critérios de aceite identificados, usaremos um formato conhecido como **Gherkin**, que utiliza palavras-chave como **"Dado"**, **"Quando"** e **"Então"** para descrever o estado inicial, a ação realizada e o resultado esperado de um cenário.

Com base nesses critérios conseguiremos evoluir para os próximos passos, definindo nossas entidades e montando os testes em cima dessa documentação.
<br><br><br>

**JOB STORY**

**Como** um usuário da CLI

**Eu quero** incluir uma lista de operações do mercado financeiro

**Para que** eu receba as informações de imposto a ser pago para cada operação
<br><br>



**CT01 - Formato Entrada**

**Dado** uma entrada de operações

**Quando** ela for ser incluida na CLI

**Então** ele deverá ser uma lista 

**E** apresentar o formato JSON 

**E** conter os seguintes campos: 
- operation *(Tipo da operação: buy, sell)*
- unit-cost *(Preço unitário da ação)* 
- quantity *(Quantidade de ações negociadas)*
<br><br>



**CT02 - Formato Saída**

**Dado** uma lista de operações processadas

**Quando** for dado o retorno para o usuário

**Então** ele deverá ser uma lista 

**E** apresentar o formato JSON

**E** conter o seguinte campo:
- tax *(Valor do imposto pago em uma operação)*
<br><br>



**CT03 - Entrada X Saída**

**Dado** uma lista de operações

**Quando** for passada uma entrada com **n** operações no formato definido

**Então** sua saída deverá ser uma lista de **n** valores de imposto, cada um calculado para cada operação de entrada
<br><br>



**CT04 - Imposto sobre operação de compra**

**Dado** uma operação de compra

**Quando** ela for analisada

**Então** não haverá imposto sobre a operação
<br><br>



**CT05 - Atualização de preço médio ponderado**

**Dado** uma operação de compra

**Quando** ela for analisada

**Então** o preço médio ponderado de compra deverá ser atualizado
<br><br>



**CT06 - Calculo preço médio ponderado**

**Dado** uma nova operação de compra

**Quando** o preço médio ponderado for ser atualizado

**Então** ele severá seguir a regra: 
- nova-media-ponderada = [(quantidade-de-acoes-atual * media-ponderadaatual) + (quantidade-de-acoes-compradas * valor-de-compra)] / (quantidade-de-acoes-atual +
quantidade-de-acoes-compradas)
<br><br>



**CT07 - Imposto sobre operação de venda**

**Dado** uma operação de venda

**Quando** o valor da operação for maior que R$20.000,00 reais 

**E** for uma operação que gerou lucro

**Então** existirá cobrança de 20% de imposto sobre o lucro da operação
<br><br>



**CT08 - Prejuízo sobre operação de venda**

**Dado** uma operação de venda

**Quando** a operação resultar em prejuízo

**Então** o prejuízo deverá ser subtraido dos lucros das operações seguintes, até que ele seja deduzido por completo
<br><br>



**CT09 - Lucro X Prejuízo em operações de venda**

**Dado** uma operação de venda

**Quando** a operação resultar em lucro após uma operação que resultou prejuízo

**Então** o prejuízo deverá ser subtraido do lucro obtido 

**E** se o resultado ainda for positivo o imposto de 20% deve ser aplicado 

**OU** se o resultado for zero o imposto será zero 

**OU** se o resultado for negativo o imposto será zero e o resto do prejuízo será subtraído da próxima operação com lucro
<br><br>



**CT10 - Arredondamento de casas decimais**

**Dado** um valor em moeda

**Quando** tiver algum valor quebrado

**Então** ele deverá ser arredondado com duas casas decimais



<br><br><br>

-------------------------------------------------------------------------------------------------------------------------------------------------------
## DDD
Como no challange temos um objetivo muito bem definido, que é o Ganho de capital, fazendo o cálculo do imposto a ser pago a partir de um conjunto de operação, conseguimos identificar somente um domínio. Com as regras e critérios de aceite já defidos acima, o nosso próximo passo será a definição das entidades. 
<br><br><br>

|OperationsList|
|--------------|
|operations: List[Operation]|
|loss: float = 0|
|operations_total_quantity: float = 0|
|tax_rate: float = 20.00|
|weighted_average_price: float|
|update_loss()|
|update_operations_total_quantity()|
|update_average_price()|
<br><br>

|Operation|
|--------------|
|type: OperationTypeEnum["buy", "sell"]|
|unity_cost: float|
|quantity: int|
|tax: float = 0.00|
<br><br>

|BuyOperation(Operation)|
|--------------|
<br><br>

|SellOperation(Operation)|
|--------------|
|total_value: float|
|return: float|
|calculate_total_value()|
|calculate_tax()|
|calculate_return()|
<br><br>