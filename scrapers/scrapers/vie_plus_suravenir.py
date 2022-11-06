import sys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

def run_vieplus_suravenir(browser):
    base_url = "https://www.previ-direct.com/web/eclient-vieplus/accueil"
    browser.get(base_url)
    # browser.maximize_window()
    
    WebDriverWait(browser, 0).until(
        EC.presence_of_element_located((By.ID, 'main-content'))
    )
    sleep(2)
    scrape_vieplus_suravenir(browser)


def scrape_vieplus_suravenir(browser):

    account_number = WebDriverWait(browser, 0).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_58_login-temp"]')))

    account_number.send_keys(sys.argv[1])

    container = WebDriverWait(browser, 0).until(EC.presence_of_element_located((By.XPATH, '//*[@id="_58_password-espace-client"]')))
    browser.execute_script("arguments[0].style.display = 'block';", container)


    secret_code = WebDriverWait(browser, 0).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_58_password"]')))
    secret_code.send_keys(sys.argv[2])

    login_submit = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_58_fm"]/div[3]/button')))

    login_submit.click()

    sleep(2)
    
    html = browser.page_source
    output = parse_html(html)
    print("output", output)


def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    account_synthese = []
    for row in soup.find_all('tr', {'class': 'portlet-section-body'}):
        if row.find('td', attrs={'class': 'table-cell'}) is not None:
            account = {}
            account["account_name"] = row.find('td', attrs={'class': 'col-1'}).text.strip()
            account["account_number"] = row.find('td', attrs={'class': 'col-2'}).text.strip()
            account["account_balance"] = row.find('td', attrs={'class': 'col-3'}).text.strip().replace(u'\xa0', u' ')
            account_synthese.append(account)
    return account_synthese