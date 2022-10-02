import chromedriver_autoinstaller
import os
import sys
import argparse

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--username")
options.add_argument("--password")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()


print('my username', sys.argv[1])
print('my secret number', sys.argv[2])

driver.get("https://connexion-mabanque.bnpparibas/login?service=%2Foauth2.0%2FcallbackAuthorize%3Fclient_id%3D0e0fe16f-4e44-4138-9c46-fdf077d56087%26redirect_uri%3Dhttps%253A%252F%252Fmabanque.bnpparibas%252Fauth%252Fon-login%26response_type%3Dcode%26state%3DdCLnBAUXwgICLMvak05CzoVk%26nonce%3DtwSB7ba3%26client_name%3DCasOAuthClient")

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#username[name='userGridPasswordCredential.username']"))).send_keys(sys.argv[1])


# print(driver.page_source)