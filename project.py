from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")  

webdriver_service = Service('C:/Users/Q1/Desktop/Modul4Final/chromedriver.exe')

driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

driver.get('https://en.wikipedia.org/wiki/NASA')

time.sleep(1)

logo_element = driver.find_element(By.XPATH, '//*[@id="siteSub"]')
logo_element.screenshot('nasa_logo.png')

table_element = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[2]')
table_element.screenshot('nasa_budget_table.png')

driver.quit()