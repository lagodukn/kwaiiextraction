# COLETAR OS INPUTS NECESSÁRIOS PARA A ENTRADA NO SITE
campaign_id = [
    {"campaign_name":"SECOM_P", "url":"https://ads.kwai.com/?accountId=60161580#/index"},
    {"campaign_name":"teste", "url":"https://ads.kwai.com/?accountId=60161580#/"},
]
for i in range(len(campaign_id)):
    print(f'--------------------\nNome da campanha: {campaign_id[i]['campaign_name']}\nId da URL da campanha: {campaign_id[i]['id']}\nURL da campanha {campaign_id[i]['url']}\n--------------------')
# ENTRARf NO SITE
import pyautogui as pg
import time 


# entra no windows
pg.press("win")
time.sleep(1)
# procura pelo chrome
pg.write("Chrome", interval=0.10)
time.sleep(1)
# abre o selecionador de perfis do chrome
pg.press("enter")
time.sleep(1)
# seleciona o perfil desejado
pg.press("tab")
time.sleep(1)
# abre o navegador
pg.press("enter")
time.sleep(1)
pg.hotkey('ctrl', 't')
pg.write(f'{campaign_id[0]['url']}', interval=0.10)
pg.press("enter")
time.sleep(7)

i = 0
while i < 7:
    print(f'{i}')
    pg.press("tab")
    time.sleep(0.5)
    i += 1
i = 0
pg.write(f'{campaign_id[0]['campaign_name']}', interval=0.10)
pg.click(x=1234, y=489, clicks=1)
time.sleep(3)
while i < 3:
    print(f'{i}')
    pg.press("tab")
    time.sleep(0.5)
    i += 1    
i = 0
pg.press("enter")
# ETAPAS DENTRO DO SITE
# COLETA DO DADO
# CONFIRMAR VERACIDADE DO DADO

