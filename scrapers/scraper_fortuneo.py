import chromedriver_autoinstaller
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--username")
options.add_argument("--password")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

print('my username', sys.argv[1])
print('my secret number', sys.argv[2])

browser.get("https://mabanque.fortuneo.fr/fr/identification.jsp")

browser.maximize_window()

time.sleep(1)

account_number = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginContainer"]/input[1]')))

account_number.send_keys(sys.argv[1])

time.sleep(2)

secret_code = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordContainer"]/span[1]/input')))
secret_code.send_keys(sys.argv[2])

time.sleep(2)

cookies_banner = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="popin_tc_privacy_button_2"]')))
cookies_banner.click()

time.sleep(2)

login_submit = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="valider_login"]')))

login_submit.click()

time.sleep(2)
# print(driver.page_source)

# quit browser
browser.quit()

