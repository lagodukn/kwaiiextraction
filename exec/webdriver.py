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

# entrada no servidor
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(f'https://ads.kwai.com/?accountId={data[0]['id']}#/report/customReport')
time.sleep(20)
driver.find_element(By.ID, "email").send_keys("performance@novasb.com.br" )
driver.find_element(By.ID, "password").send_keys("$NOVASB$2022@")
driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[2]/div[2]/button").click()
time.sleep(20)

# setup de datas para periodo de analise
start_date = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/input')
end_date = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[3]/input')
start_date.send_keys(Keys.CONTROL+"A")
time.sleep(2)
start_date.send_keys(f'{data[0]['startdate']}')
time.sleep(2)
end_date.send_keys(Keys.CONTROL+"A")
time.sleep(2)
end_date.send_keys(f'{date.today()}')
end_date.send_keys(Keys.ENTER)
time.sleep(2)

# entrada de exec para coletar o dado
export_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div[2]/button')
true_exportation = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/div[2]/div[1]/button')
export_button.click()
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div/div[2]').click()
time.sleep(2)
true_exportation.click()
time.sleep(5)
# looping de suporte para a coleta correta do dado

# Encontre a tabela
tabela = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div/div/div[2]/div/div/div/div/div/div/table/tbody')

# Encontre todas as linhas (trs) da tabela
linhas = tabela.find_elements(By.TAG_NAME, 'tr')
# Itere sobre as linhas
for linha in linhas:
     # Encontre todas as colunas (tds) da linha
    colunas = linha.find_elements(By.TAG_NAME, 'td')
    print(colunas)
driver.quit()
    # Verifique se a data na coluna é coerente com a data que você está procurando
    # data_coluna = colunas[1].text  # supondo que a data esteja na primeira coluna
    # print(data_coluna)
    # if data_coluna == date.today():
    #     # Encontre o link (a) com o atributo href
    #     link = linha.find_element(By.TAG_NAME, 'a')
    #     href = link.get_attribute('href')
        
    #     # Faça algo com o link (por exemplo, clique nele)
    #     driver.get(href)
    #     break