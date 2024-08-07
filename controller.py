# controlar a entrada e saida de funcoes dentro do sistema. 

# nao se esquecer de criar um dotenv para dar o handle nos dados que nao devem estar no codigo, como logins e senhas, bem como 
# os dados das campanhas antigas e novas... 

# nao esquecer de adicionar ao input a pergunta de que "posso coletar desta campanha?", ou algo como "ela já acabou?

# sendo que a primeira entrada será checar a existencia de config.json e executar as funcoes que estao em input
# sendo assim, chamar o robo que vai passear dentro do site e coletar os devidos dados
# logo após, coletar os dados e comparar com a tabela existente, para assim poder trocar os dados de lugar

from exec.webdriver import load_config, setup_driver, login, setup_inside
from dotenv import load_dotenv
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

enter = os.getenv("PROFILE_EMAIL")
passw = os.getenv("PROFILE_PASS")

options = Options() 
driver = webdriver.Chrome(options=options)
driver.maximize_window()
time.sleep(40)
