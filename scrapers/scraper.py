import chromedriver_autoinstaller
import sys
import datetime
from time import time, sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--username")
    options.add_argument("--password")
    options.add_argument("--headless")
    if len(sys.argv) > 3  and sys.argv[3] == "headless":
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    else:
        chromedriver_autoinstaller.install()
        sleep(2)
        browser = webdriver.Chrome(chrome_options=options)
    return browser

def run_fortuneo(browser):
    base_url = "https://mabanque.fortuneo.fr/fr/identification.jsp"
    browser.get(base_url)
    browser.maximize_window()
    
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.ID, 'acces_client'))
    )
    scrape()


def scrape():

    account_number = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginContainer"]/input[1]')))

    account_number.send_keys(sys.argv[1])

    secret_code = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordContainer"]/span[1]/input')))
    secret_code.send_keys(sys.argv[2])

    cookies_banner = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popin_tc_privacy_button_2"]')))
    cookies_banner.click()

    login_submit = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="valider_login"]')))

    login_submit.click()

    # display bank account blocked by iframe
    iframe = WebDriverWait(browser, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="iframe_centrale"]')))
    
    html = browser.page_source
    output = parse_html(html)
    # print(output)


def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    print(soup.prettify())
    # account_synthese = []
    return []


if __name__ == "__main__":
    print('my username', sys.argv[1])
    print('my secret number', sys.argv[2])

    start_time = time()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    browser = get_driver()

    run_fortuneo(browser)
    
    # Close the browser
    browser.quit()
    end_time = time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")


