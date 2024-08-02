import time
import os
import json
import pyautogui as pg
from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


if os.path.exists('config.json'):
    with open('config.json', 'r') as f:
        data = json.load(f)
else:
    print('Não foi possível encontrar os dados de Configuração.')

chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(f'https://ads.kwai.com/?accountId={data[0]['id']}#/report/customReport')
time.sleep(20)

driver.find_element(By.ID, "email").send_keys("performance@novasb.com.br" )
driver.find_element(By.ID, "password").send_keys("$NOVASB$2022@")
driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(30)

start_date = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/input')
start_date.send_keys(Keys.CONTROL+"A")
time.sleep(2)
start_date.send_keys(f'{data[0]['startdate']}')
pg.press('tab')
time.sleep(0.5)
pg.press('tab')
pg.write(f'{date.today()}')