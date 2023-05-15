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

**E** se o resultado ainda for positivo e maior que R$20.000,00 o imposto de 20% deve ser aplicado

**OU** se o resultado for zero o imposto será zero

**OU** se o resultado for negativo o imposto será zero e o resto do prejuízo será subtraído da próxima operação com lucro
<br><br>



**CT10 - Arredondamento de casas decimais**

**Dado** um valor em moeda

**Quando** tiver algum valor quebrado

**Então** ele deverá ser arredondado com duas casas decimais



<br><br><br>

-------------------------------------------------------------------------------------------------------------------------------------------------------
## **DDD**
Como no challange temos um objetivo muito bem definido, que é o Ganho de capital, fazendo o cálculo do imposto a ser pago a partir de um conjunto de operação, conseguimos identificar somente um domínio. Com as regras e critérios de aceite já defidos acima, o nosso próximo passo será a definição das entidades e os objetos de valor.
<br><br><br>

### **Entidades**
- Uma Entidade representa um objeto do domínio com identidade própria e um ciclo de vida distinto
- Ela é definida por suas características e comportamentos, além de ter um identificador exclusivo.
<br><br>

|OperationsList|
|--------------|
|operations: List [OperationCapitalGain]|

Essa é a entidade que irá tratar do conjunto de operações realizados a cada entrada, contendo todas as informações passadas na entranda, assim como os seus impostos calculados.
<br><br>

|Operation|
|--------------|
|type: OperationTypeEnum["buy", "sell"]|
|unity_cost: float|
|quantity: int|

Nessa entidade temos uma generalização de operação, contendo os dados básicos para a existência dela. Essa generalização foi pensada de modo a classe de operação poder ser extensível a outros tipos de utilização.
<br><br>

|OperationCapitalGain(Operation)|
|--------------|
|operations_total_quantity: int|
|operation_weighted_average_price: float|
|new_operations_total_quantity: int|
|new_operation_weighted_average_price: int|
|tax: Tax|

Nessa entidade temos uma filha de operação, específica para utilização para o ganho de capital.
<br><br>

|BuyOperationCapitalGain(OperationCapitalGain)|
|--------------|

Nessa entidade temos uma filha de operação de ganho de capital, específica para compra, contendo especificações de compra sem alteração das classes mãe.
<br><br>

|sellOperationCapitalGain(OperationCapitalGain)|
|--------------|
|returns: Return|
|total_value: float|
|previous_loss: Optional[float]|

Nessa entidade temos uma filha de operação de ganho de capital, específica para venda, contendo especificações de venda sem alteração das classes mãe.
<br><br>

### **Objetos de valor**
- Um Objeto de Valor representa um conceito ou um valor no domínio que é identificado por suas propriedades.
- Ele é caracterizado por seus atributos e não possui uma identidade própria.
- Os Objetos de Valor são imutáveis, ou seja, uma vez criados, seus atributos não são alterados.
- Geralmente, os Objetos de Valor são pequenos e são usados para encapsular um conjunto de propriedades relacionadas.
<br><br>


|Returns|
|--------------|
|average_price: float|
|quantity: float|
|total_value: float|
|returns: float|

Nesse objeto de valor, temos uma generalização para o resultado de uma operação, podendo ser positivo (Lucro) ou negativo (Prejuízo) a partir das informações de preço médio, quantidade, valor total da operação, e o valor do resultado. Foi criado como objeto de valor a fim de ser uma propriedade padrão para resultado idependentemente de sua aplicação.
<br><br>

|Tax|
|--------------|
|value: float|
|tax_rate: float|
|tax_value: float = self.value * self.tax_rate|

Nesse objeto de valor, temos uma generalização para o imposto, a partir das informações de valor, percentagem do imposto e o valor de imposto resultante. Foi criado como objeto de valor a fim de ser uma propriedade padrão para imposto idependentemente de sua aplicação.
<br><br><br>

-------------------------------------------------------------------------------------------------------------------------------------------------------
## **Bibliotecas**
As biblioticas e dependencias usadas no projeto em sua maioria, serão para teste e para linter, afim de garantir uma maior qualidade de código, porém conforme solicitado durante a implementação da solução do desafio será utilizado o mínimo de bibliotecas possíveis, com o objetivo de deixar claro o raciocínio por tras da lógica.

### **Poetry**
Poetry é uma ferramenta para gerenciamento de pacotes e dependências para Python. Iremos utiliza-la para facilitar a adição de novas depências, assim como o controle de suas versões.

### **Pytest**
Framework para escrita de testes unitários em python.

### **Covarage**
O Coverage.py é uma ferramenta para medir a cobertura de código de programas em Python.

### **Pydantic**
Pydantic é uma biblioteca de Python usada para validação de dados.

### **Pre-commit**

- **Black:**
Formatador de código para python

- **Autoflake:**
Remove imports e variaveis que não foram utilizados

- **Isort:**
Organiza os imports por ordem alfabética e automaticamente separa em seções e por tipo

- **Flake8:**
Validador de Pep8 (Style Guide para códigos em python)

- **Mypy:**
Validador de tipagem

- **Yesqa:**
Remove automaticamente comentários # noqa desnecessários
<br><br><br>

-------------------------------------------------------------------------------------------------------------------------------------------------------
## **Arquitetura**

A arquitetura de software escolhida para o challange será a arquitetura limpa.

### **Sobre a arquitetura**
A arquitetura limpa (clean architecture) é um padrão de arquitetura de software proposto por Robert C. Martin, também conhecido como Uncle Bob. Ela busca separar as preocupações em um sistema, promovendo um design modular, testável e de fácil manutenção.

A principal ideia por trás da arquitetura limpa é estabelecer uma separação clara e definida entre as diferentes camadas do sistema, com cada camada tendo responsabilidades específicas e bem definidas. Essa separação permite que as camadas internas não dependam das camadas externas, resultando em um acoplamento fraco e maior flexibilidade.

A arquitetura limpa segue o princípio da inversão de dependência (Dependency Inversion Principle - DIP) e do princípio da responsabilidade única (Single Responsibility Principle - SRP). O princípio da inversão de dependência prega que módulos de alto nível não devem depender de módulos de baixo nível, mas sim de abstrações. Já o princípio da responsabilidade única afirma que cada classe ou componente deve ter apenas uma razão para mudar.

### **Estrutura**
A arquitetura limpa é composta por várias camadas, que geralmente incluem:

- **domain**: Camada de domínio, é o núcleo do sistema e contém as regras de negócio e as entidades principais.

- **application**: Camada de aplicação, é responsável por orquestrar as ações do sistema, aplicando as regras de negócio da camada de entidades.

- **adpter_entrypoints**: É a camada responsável por lidar com a interação do usuário, seja por meio de uma interface gráfica, uma API ou qualquer outro meio de comunicação.

- **infrastructure**: É a camada responsável por implementar os detalhes técnicos, como acesso a bancos de dados, chamadas a serviços externos, etc.

### **Motivos**
A escolha da arquitetura limpa foi pensada por dois motivos.
- Por ela ser uma arquitetura com um fraco acoplamento entre as camadas, ela facilita a manutenção e também a escalabilidade do sistema, por esse desafio poder ser estendido futuramente, ela se faz uma boa opção, permitindo uma facilidade para inclusão de novas features.
- Também foi escolhida por ser a arquitetura que estou utilizando atualmente, agilizando assim o desenvolvimento baseado no prazo de entrega do projeto.
<br><br><br>

-------------------------------------------------------------------------------------------------------------------------------------------------------
## **Dockerização**

O projeto foi dockerizado, com o objetivo de facilitar a utilização em qualquer máquina.

Temos um único container (*cli*), que é utilizado para suir a aplicação baseada no docker-compose e um Dockerfile que faz todas as configurações de ambiente para o projeto.
<br><br><br>

-------------------------------------------------------------------------------------------------------------------------------------------------------
## **Como rodar o projeto**


### **Utilizando Docker**
Para rodar o projeto com docker, é necessário ter ele instalado na sua máquina, caso não tenha, siga as instruções dos links:
- **Ubuntu:** [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
- **Mac:** [Install Docker Engine on Mac](https://docs.docker.com/desktop/install/mac-install/)
- **Windows:** [Install Docker Engine on Windows](https://docs.docker.com/desktop/install/windows-install/)

Comece buildando e subindo seu container:
```
docker compose up -d --build
```

Se a sua versão do docker-compose for mais antiga, use:
```
docker-compose up -d --build
```
Para rodar o projeto utilizando um arquivo, inclua o arquivo na root do projeto em seguida rode os seguintes comandos:
```
docker run -i ganho-capital-cli < nome_arquivo.txt
```

Para rodar o projeto fazendo input manualmente  rode os seguintes comandos:
```
docker run -i ganho-capital-cli
```

### **Utilizando poetry**
Para rodar o projeto com poetry, é necessário ter ele instalado na sua máquina, caso não tenha, siga as instruções dos links:
[Install Poetry](https://python-poetry.org/docs/#:~:text=To%20uninstall%20Poetry%2C%20simply%20delete%20the%20entire%20%24VENV_PATH%20directory.)


Comece criando sua env e instalando suas dependencias:
```
poetry install
```

Em seguida use o comando:
```
poetry run python -m system
```

Para rodar o projeto utilizando um arquivo, inclua o arquivo na root do projeto em seguida rode os seguintes comandos:
```
poetry run python -m system < nome_arquivo.txt
```
<br><br><br>

-------------------------------------------------------------------------------------------------------------------------------------------------------
## **TDD**
O projeto foi feito utilizando a estratégia de desenvolvimento de Test-Driven Development, que se baseia em um ciclo curto de repetições que consiste em Escrever o teste, Escrever o código e Refatorar o código.

Os testes foram criados em cima dos critérios de aceite deifinidos acima, que foram montados de acordo com a documentação do challange.

Para rodar o testes utilize o comando:
```
poetry run pytest

#OU

poetry run pytest -vvv
```

Também foi utilizada a biblioteca coverage para testes em python para ver a cobertura dos testes automatizados.

Para ver o relatorio do coverage basta rodar o seguinte comando:
```
poetry run coverage report

```
<br><br><br>

-------------------------------------------------------------------------------------------------------------------------------------------------------
## **Informações adicionais**

O projeto foi feito com bastante carinho, usando todas as boas práticas utilizadas no dia a dia de trabalho, com o objetivo de ficar facilmente entendível, com as obgrigações de todas as classes e métodos bem segregadas, possibilitando assim a extensão do projeto se possível, da maneira mais simples possível, porém focando em uma boa estruturação.

**Agradecimento especial** ao chat gpt que me acompanhou nessa jornada! <3

Agradeço a você que leu até aqui, espero que tenha sido um projeto divertido de acompanhar e avaliar!
