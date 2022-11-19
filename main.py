from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import RAINBOW_LINK

from datetime import datetime as dt

import time
import warnings


CHROME_DRIVER = "chromedriver\chromedriver.exe"

def fill_form(driver, email_address):
        email = WebDriverWait(driver, 20, 0.05).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
        email.send_keys(email_address)

        WebDriverWait(driver, 20, 0.05).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="main"]/div/div[1]/div[4]/div[2]/div[3]/div[1]/div/div/div[2]/div/div[2]/div/div'))).click()

def launch_swd():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument("--disable-extensions")
    options.add_argument("--output=/dev/null")
    options.add_argument("--log-level=3")
    options.add_argument("--headless")
    options.add_argument("--disable-crash-reporter")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-in-process-stack-traces")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    warnings.filterwarnings("ignore", category=DeprecationWarning) 
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER, chrome_options=options)
    return driver

def main():
    with open("mails.txt", "r") as file:
        iterator = 1
        for mail in file:
            driver = launch_swd()
            driver.maximize_window()
            driver.get(RAINBOW_LINK)

            email_address = mail.split(':')

            print(f"{dt.now().time()} Ввожу аккаунт #{iterator}")

            fill_form(driver, email_address[0])
            time.sleep(20)

            print(f"{dt.now().time()} Завершаю работу #{iterator}")
            
            driver.quit()

            iterator += 1

if __name__ == "__main__":
    main()


        