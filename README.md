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

`finance_scraper.py`: Contém a classe `FinanceCrawler`, responsável pela lógica de extração dos dados utilizando Selenium e BeautifulSoup.
`utils.py`: Funções utilitárias, como formatação dos dados e escrita no arquivo CSV.
`test_crawler.py`: Implementação de testes unitários para validar o funcionamento do crawler.

## Instalação e Configuração

### Pré-requisitos
Certifique-se de ter o Python 3.8+ instalado em sua máquina e o navegador Google Chrome (ou outro navegador compatível) instalado.

### Passos para Instalação

**1. Clonar o repositório:**

```
git clone https://github.com/seu-usuario/crawler-financeiro.git
cd crawler-financeiro

**2. Criar um ambiente virtual (opcional, mas recomendado):**

```
python -m venv venv
venv\Scripts\activate  # Para Windows

**3. Instalar as dependências**: As dependências do projeto estão listadas no arquivo requirements.txt. Para instalá-las, execute:

```
pip install -r requirements.txt

**4. Configurar o WebDriver**: Baixe a versão correta do ChromeDriver para o seu navegador e coloque-o no PATH ou configure diretamente no código. Consulte a documentação do Selenium para detalhes: Selenium WebDriver.

### Executando o Crawler
Para executar o crawler e obter os dados de uma região específica, use o seguinte comando:

```
python finance_scraper.py

Isso gerará um arquivo CSV com os resultados da busca na pasta do projeto.

### Exemplo de Execução
Ao buscar pelos dados da região "Argentina", o arquivo CSV gerado terá o seguinte conteúdo:

```
"symbol","name","price"
"AMX.BA","América Móvil, S.A.B. de C.V.","2089.00"
"NOKA.BA","Nokia Corporation","557.50"

## Testes Unitários
Para garantir a qualidade do código, foram implementados testes unitários utilizando a biblioteca pytest. Para rodar os testes, basta executar o seguinte comando:

