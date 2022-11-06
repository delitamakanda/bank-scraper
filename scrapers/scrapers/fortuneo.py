import sys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def run_fortuneo(browser):
    base_url = "https://mabanque.fortuneo.fr/fr/identification.jsp"
    browser.get(base_url)
    # browser.maximize_window()
    
    WebDriverWait(browser, 0).until(
        EC.presence_of_element_located((By.ID, 'acces_client'))
    )
    sleep(2)
    scrape_fortuneo(browser)


def scrape_fortuneo(browser):

    account_number = WebDriverWait(browser, 0).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginContainer"]/input[1]')))

    account_number.send_keys(sys.argv[1])

    secret_code = WebDriverWait(browser, 0).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordContainer"]/span[1]/input')))
    secret_code.send_keys(sys.argv[2])

    cookies_banner = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popin_tc_privacy_button_2"]')))
    cookies_banner.click()

    login_submit = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="valider_login"]')))

    login_submit.click()

    sleep(2)

    # display bank account blocked by iframe
    iframe = WebDriverWait(browser, 40).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="iframe_centrale"]')))
    
    html = browser.page_source
    output = parse_html(html)
    print("output", output)


def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    account_synthese = []
    for row in soup.find_all('tr', {'class': 'synthese_compte_ligne_num_compte'}):
        if row.find('a', attrs={'class': 'synthese_id_compte'}) is not None:
            account = {}
            title = row.find('a', attrs={'class': 'synthese_id_compte'}).text.strip().replace(u'\xa0', u' ')
            account["account_name"] = ' '.join(title.split())
            account["account_number"] = row.find('span', attrs={'class': 'synthese_numero_compte'}).text.strip()
            account["account_balance"] = row.find('span', attrs={'class': 'synthese_solde_compte'}).text.strip().replace(u'\xa0', u' ')
            account_synthese.append(account)
    return account_synthese