import os
import time

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class FinanceScraper:
    def __init__(self):
        # Configurações do navegador Firefox
        firefox_options = Options()
        firefox_options.add_argument('--ignore-certificate-errors')
        firefox_options.add_argument('--ignore-ssl-errors')

        # Inicializando o navegador
        self.driver = webdriver.Firefox(options=firefox_options)
        self.wait = WebDriverWait(self.driver, 20)

        # Acessar a URL
        base_url = "https://finance.yahoo.com/screener/new"
        self.driver.get(base_url)

        # Esperar pelo botão 'Region' e clicar
        region_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Region']"))
        )
        region_button.click()
        print("Botão 'Region' clicado.")
        
        # Esperar pelo botão 'Add Region' e clicar
        add_region_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[1]/div/div[2]/ul/li[2]/button'))
        )
        add_region_button.click()
        print("Botão 'Add Region' clicado.")
        
        # Esperar que a lista de países apareça
        time.sleep(3)

        # Desmarcar 'United States' antes de solicitar o país ao usuário
        self.deselect_united_states()

    def deselect_united_states(self):
        try:
            # Desmarcar 'United States' (posição 54)
            us_checkbox = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="dropdown-menu"]/div/div[2]/ul/li[54]/label'))
            )
            us_checkbox.click()
            print("País 'United States' desmarcado.")
        except Exception as e:
            print(f"Erro ao desmarcar 'United States': {e}")

    def select_country(self, country_xpath):
        try:
            # Selecionar o país baseado no XPath passado
            country_checkbox = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, country_xpath))
            )
            country_checkbox.click()
            print("País selecionado.")
            
            # Esperar pelo botão de "Find Stocks" e clicar
            find_stocks_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="screener-criteria"]/div[2]/div[1]/div[3]/button[1]'))
            )
            find_stocks_button.click()
            print("Botão 'Find Stocks' clicado para realizar a pesquisa.")
            
            # Esperar até que os resultados da pesquisa sejam exibidos
            time.sleep(5)

        except Exception as e:
            print(f"Erro durante a execução: {e}")

    
    def get_page_source(self):
        return self.driver.page_source

    def parse_html(self, html: str):
        if html is None:
            print("Erro: O HTML não foi obtido corretamente.")
            return []
        
        soup = BeautifulSoup(html, 'html.parser')
        
        # Buscar as linhas da tabela com os dados
        rows = soup.find_all('tr', class_="simpTblRow")
        data = []
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 3:
                symbol = cols[0].text.strip()
                name = cols[1].text.strip()
                price = cols[2].text.strip()
                data.append({"symbol": symbol, "name": name, "price": price})
        
        return data

    def save_to_csv(self, data, region):
        if not data:
            print("Nenhum dado foi extraído.")
            return

        # Criar a pasta output se não existir
        output_folder = "output"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Especificando o formato correto com aspas e separador por vírgula
        output_csv = os.path.join(output_folder, f"{region.lower().replace(' ', '_')}.csv")
        
        # Salvando em CSV com aspas e delimitador correto
        df = pd.DataFrame(data)
        df.to_csv(output_csv, index=False, quotechar='"', quoting=1, sep=',')
        print(f"Dados salvos em {output_csv}")

    def scrape(self, region):
        html = self.get_page_source()
        if html:
            data = self.parse_html(html)
            self.save_to_csv(data, region)
        self.driver.quit()


if __name__ == "__main__":
    scraper = FinanceScraper()

    # Opções de países e seus respectivos XPaths
    countries = {
        1: ('Argentina', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[1]/label'),
        2: ('Austria', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[2]/label'),
        3: ('Australia', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[3]/label'),
        4: ('Belgium', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[4]/label'),
        5: ('Brazil', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[5]/label'),
        6: ('Canada', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[6]/label'),
        7: ('Switzerland', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[7]/label'),
        8: ('Chile', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[8]/label'),
        9: ('China', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[9]/label'),
        10: ('Czechia', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[10]/label'),
        11: ('Germany', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[11]/label'),
        12: ('Denmark', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[12]/label'),
        13: ('Estonia', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[13]/label'),
        14: ('Egypt', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[14]/label'),
        15: ('Spain', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[15]/label'),
        16: ('Finland', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[16]/label'),
        17: ('France', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[17]/label'),
        18: ('United Kingdom', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[18]/label'),
        19: ('Greece', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[19]/label'),
        20: ('Hong Kong SAR China', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[20]/label'),
        21: ('Hungary', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[21]/label'),
        22: ('Indonesia', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[22]/label'),
        23: ('Ireland', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[23]/label'),
        24: ('Israel', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[24]/label'),
        25: ('India', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[25]/label'),
        26: ('Iceland', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[26]/label'),
        27: ('Italy', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[27]/label'),
        28: ('Japan', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[28]/label'),
        29: ('South Korea', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[29]/label'),
        30: ('Kuwait', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[30]/label'),
        31: ('Sri Lanka', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[31]/label'),
        32: ('Lithuania', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[32]/label'),
        33: ('Latvia', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[33]/label'),
        34: ('Mexico', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[34]/label'),
        35: ('Malaysia', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[35]/label'),
        36: ('Netherlands', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[36]/label'),
        37: ('Norway', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[37]/label'),
        38: ('New Zealand', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[38]/label'),
        39: ('Peru', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[39]/label'),
        40: ('Philippines', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[40]/label'),
        41: ('Pakistan', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[41]/label'),
        42: ('Poland', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[42]/label'),
        43: ('Portugal', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[43]/label'),
        44: ('Qatar', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[44]/label'),
        45: ('Romania', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[45]/label'),
        46: ('Russia', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[46]/label'),
        47: ('Saudi Arabia', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[47]/label'),
        48: ('Sweden', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[48]/label'),
        49: ('Singapore', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[49]/label'),
        50: ('Suriname', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[50]/label'),
        51: ('Thailand', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[51]/label'),
        52: ('Turkey', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[52]/label'),
        53: ('Taiwan', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[53]/label'),
        54: ('United States', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[54]/label'),
        55: ('Venezuela', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[55]/label'),
        56: ('Vietnam', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[56]/label'),
        57: ('South Africa', '//*[@id="dropdown-menu"]/div/div[2]/ul/li[57]/label'),
    }

    # Apresentar opções ao usuário
    print("Escolha um país para consulta:")
    for key, value in countries.items():
        print(f"{key} - {value[0]}")

    # Receber a escolha do usuário
    choice = int(input("Digite o número do país escolhido: "))

    # Selecionar o país e realizar a pesquisa
    if choice in countries:
        scraper.select_country(countries[choice][1])
        scraper.scrape(countries[choice][0])
    else:
        print("Opção inválida.")
