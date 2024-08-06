import time
import os
import json
from datetime import date, datetime
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv
import pandas as pd
from tabulate import tabulate

load_dotenv()
enterkey = os.getenv("EMAIL")
enterpass = os.getenv("PASS")
enterurl = os.getenv("URL")
enterurlf = os.getenv("URLAST")

def load_config():
    if os.path.exists('config.json'):
        with open('config.json', 'r') as f:
            return json.load(f)
    else:
        print('Não foi possível encontrar os dados de Configuração.')
        return None
    
def setup_driver(config, director):
    try:
        chrome_options = Options() 
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(f'{enterurl}{config[director]['id']}#/{enterurlf}')
        time.sleep(20)
    except:
        print('Deu ruim de entrar no site')
    return driver

def login(driver):
    driver.find_element(By.ID, "email").send_keys(enterkey)
    driver.find_element(By.ID, "password").send_keys(enterpass)
    driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[2]/div[2]/button").click()
    time.sleep(20)

def setup_inside(driver, config, director):
    start_date = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/input')
    end_date = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[3]/input')
    start_date.send_keys(Keys.CONTROL+"A")
    time.sleep(2)
    start_date.send_keys(f'{config[director]['startdate']}')
    time.sleep(2)
    end_date.send_keys(Keys.CONTROL+"A")
    time.sleep(2)
    end_date.send_keys(f'{date.today()}')
    end_date.send_keys(Keys.ENTER)
    time.sleep(2)
    export_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div[2]/button')
    true_exportation = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/div[2]/div[1]/button')
    export_button.click()
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div/div[2]').click()
    time.sleep(2)
    true_exportation.click()
    time.sleep(5)
    tabela = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div/div/div[2]/div/div/div/div/div/div/table/tbody')
    linhas = tabela.find_elements(By.TAG_NAME, 'tr')
    for linha in linhas:
        colunas = linha.find_elements(By.TAG_NAME, 'td')
        for i, coluna in enumerate(colunas):
            data_str = coluna.text
            padrao = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$")
            if padrao.match(data_str):
                data_real = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
                hora_real = data_real.time()
                hora_atual = datetime.now().time()
                if data_real.date() == date.today() and hora_real.hour == hora_atual.hour and hora_real.minute >= hora_atual.minute - 2:
                    target = colunas[i + 2].click()
                    time.sleep(30)
                    break
    driver.get('chrome://downloads/')
    time.sleep(20)
    # Get the latest downloaded file
    downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
    files = os.listdir(downloads_dir)
    files.sort(key=lambda x: os.path.getmtime(os.path.join(downloads_dir, x)))
    latest_file = files[-1]

    # Read the Excel file
    last = os.path.join(downloads_dir, latest_file)
    sheets_comparison(last)
    return 

def sheets_comparison(last):
    df = pd.ExcelFile(last)
    sheet_names = df.sheet_names
    second = sheet_names[1]
    df = df.parse(second)
    print(tabulate(df.iloc[:,1:], headers='keys', tablefmt='psql'))
    

def main():
    config = load_config()
    if config:
        popup = tk.Tk()
        popup.title("Selecione a campanha a ser extraída")
        largura = 300
        altura = 200
        popup.geometry(f"{largura}x{altura}")
        label = tk.Label(popup, text='Selecione o nome da campanha: ')
        label.pack()
        nomes = [item['nome'] for item in config]
        indice_var = tk.StringVar()
        indice_var.set(nomes[0])
        option = ttk.OptionMenu(popup, indice_var, *nomes)
        option.pack()

        def exec_script():
            director = nomes.index(indice_var.get())
            driver = setup_driver(config, director)
            login(driver)
            setup_inside(driver, config, director)
            #last = setup_inside(driver, config, director)
            #sheets_comparison(last)
            driver.quit()
            popup.destroy()
        button = tk.Button(popup, text='Executar', command=exec_script)
        button.pack()
        popup.mainloop()

if __name__ == '__main__':
    main()

config = load_config()