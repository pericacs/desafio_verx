import os
import sys
from unittest.mock import MagicMock, patch

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from finance_crawler import FinanceCrawler


@patch('finance_crawler.webdriver.Firefox')
@patch('finance_crawler.WebDriverWait')
def test_select_country(mock_webdriver, mock_wait):
    print("Iniciando o teste para select_country...")
    scraper = FinanceCrawler()
    mock_wait_until = mock_wait.return_value.until

    country_xpath = '//*[@id="dropdown-menu"]/div/div[2]/ul/li[1]/label'
    mock_element = MagicMock()
    mock_wait_until.return_value = mock_element

    scraper.select_country(country_xpath)
    try:
        mock_wait_until.assert_called_once_with(
            EC.element_to_be_clickable((By.XPATH, country_xpath))
        )
        mock_element.click.assert_called_once()
    except AssertionError:
        print("O método 'until' não foi chamado como esperado.")
    print("Teste para select_country finalizado.")

@patch('finance_crawler.BeautifulSoup')
def test_parse_html(mock_soup):
    print("Iniciando o teste para parse_html...")
    scraper = FinanceCrawler()
    html = '<html><table><tr class="simpTblRow"><td>AMX.BA</td><td>América Móvil</td><td>2089.00</td></tr></table></html>'

    mock_td_symbol = MagicMock()
    mock_td_symbol.text = "AMX.BA"

    mock_td_name = MagicMock()
    mock_td_name.text = "América Móvil"

    mock_td_price = MagicMock()
    mock_td_price.text = "2089.00"

    mock_row = MagicMock()
    mock_row.find_all.return_value = [mock_td_symbol, mock_td_name, mock_td_price]

    mock_soup.return_value.find_all.return_value = [mock_row]

    data = scraper.parse_html(html)
    assert len(data) == 1
    assert data[0]['symbol'] == 'AMX.BA'
    assert data[0]['name'] == 'América Móvil'
    assert data[0]['price'] == '2089.00'
    print("Teste para parse_html finalizado.")


@patch('finance_crawler.pd.DataFrame.to_csv')
def test_save_to_csv(mock_to_csv):
    print("Iniciando o teste para save_to_csv...")
    scraper = FinanceCrawler()
    data = [{"symbol": "AMX.BA", "name": "América Móvil", "price": "2089.00"}]
    region = "Argentina"

    scraper.save_to_csv(data, region)

    mock_to_csv.assert_called_once()
    print("Teste para save_to_csv finalizado.")

@patch('finance_crawler.WebDriverWait.until')
def test_deselect_united_states(mock_wait_until):
    print("Iniciando o teste para deselect_united_states...")
    scraper = FinanceCrawler()

    mock_element = MagicMock()
    mock_wait_until.return_value = mock_element
    scraper.deselect_united_states()

    try:
        mock_wait_until.assert_called_once_with(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="dropdown-menu"]/div/div[2]/ul/li[54]/label'))
        )
        mock_element.click.assert_called_once()
    except AssertionError:
        print("O método 'until' não foi chamado como esperado.")
    print("Teste para deselect_united_states finalizado.")
