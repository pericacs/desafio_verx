# Desafio: Teste Desenvolvedor Python - Crawler Financeiro

Este projeto é parte do desafio proposto para a vaga de Desenvolvedor Python. O objetivo principal é desenvolver um **crawler** utilizando as bibliotecas **Selenium**, **BeautifulSoup** e aplicando os princípios de **orientação a objetos**. O crawler deve capturar informações de ações de diferentes regiões do site **Yahoo Finance** e salvar os dados em um arquivo CSV.

## Objetivo do Projeto

O desafio consiste em criar um crawler em Python que:
1. Acesse o site [Yahoo Finance Screener](https://finance.yahoo.com/screener/new).
2. Extraia os seguintes dados:
   - **Nome da ação** (`name`)
   - **Símbolo da ação** (`symbol`)
   - **Preço intraday da ação** (`price (intraday)`)
3. O crawler deve receber como parâmetro de entrada a **região** (ex: `Argentina`), aplicando este filtro para obter os dados relevantes.
4. A saída do crawler deve ser salva em um arquivo CSV com o seguinte formato:

   ```csv
   "symbol","name","price"
   "AMX.BA","América Móvil, S.A.B. de C.V.","2089.00"
   "NOKA.BA","Nokia Corporation","557.50"

## Tecnologias Utilizadas

- **Python 3.8+**: Linguagem de programação principal.
- **Selenium**: Para automação do navegador e captura de dados dinâmicos.
- **BeautifulSoup**: Para análise e extração dos dados HTML.
- **Orientação a Objetos (OOP)**: Para estruturação e organização do código.
- **pytest**: Implementação de testes unitários (diferencial).


## Arquivos principais

`finance_crawler.py`: Contém a classe `FinanceCrawler`, responsável pela lógica de extração dos dados utilizando Selenium e BeautifulSoup.
`test_finance_crawler.py`: Implementação de testes unitários para validar o funcionamento do crawler.

## Instalação e Configuração

### Pré-requisitos
Certifique-se de ter o Python 3.8+ instalado em sua máquina e o navegador Firefox Mozilla instalado.

### Passos para Instalação

**1. Clonar o repositório:**

```
git clone https://github.com/pericacs/desafio_verx.git
cd desafio_verx
```

**2. Criar um ambiente virtual (opcional, mas recomendado):**

```
python -m venv venv
venv\Scripts\activate  # Para Windows
```
**3. Instalar as dependências**: As dependências do projeto estão listadas no arquivo requirements.txt. Para instalá-las, execute:

```
pip install -r requirements.txt
```
**4. Configurar o WebDriver**: Baixe a versão correta do geckodriver para o seu navegador mozilla e coloque-o no PATH ou configure diretamente no código. Consulte a documentação do Selenium para detalhes: Selenium WebDriver.

### Executando o Crawler
Para executar o crawler e obter os dados de uma região específica, use o seguinte comando:

```
python finance_crawler.py
```
Como possuem alguns paises para escolher, o robo vai perguntar qual o pais a sua escolha as opções dos paises são numericas, 
exemplo: Se quer consultar por Argentina, digitar "1" então o filtro é preenchido com o pais e a consulta realizada, buscando as informações para a geração do arquivo CSV com os resultados da busca na pasta "output" do projeto.

### Exemplo de Execução
Ao buscar pelos dados da região "Argentina", o arquivo CSV gerado terá o seguinte conteúdo:

```
"symbol","name","price"
"AMX.BA","América Móvil, S.A.B. de C.V.","2089.00"
"NOKA.BA","Nokia Corporation","557.50"
```
## Testes Unitários

Para garantir a qualidade do código, foram implementados testes unitários utilizando a biblioteca pytest. Para rodar os testes, basta executar o seguinte comando:

```
pytest tests/test_finance_crawler.py
```
