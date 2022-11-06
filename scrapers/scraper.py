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
from scrapers.fortuneo import run_fortuneo
from scrapers.vie_plus_suravenir import run_vieplus_suravenir

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--username")
    options.add_argument("--password")
    options.add_argument("--bank")
    options.add_argument("--headless")
    if len(sys.argv) > 4  and sys.argv[4] == "headless":
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    else:
        chromedriver_autoinstaller.install()
        sleep(2)
        browser = webdriver.Chrome(chrome_options=options)
    return browser




if __name__ == "__main__":
    print('my username', sys.argv[1])
    print('my secret number', sys.argv[2])
    print('bank', sys.argv[3])

    start_time = time()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    browser = get_driver()

    if sys.argv[3] == "fortuneo":
        run_fortuneo(browser)
    elif sys.argv[3] == "vieplus":
        run_vieplus_suravenir(browser)
    
    # Close the browser
    browser.quit()
    end_time = time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")


