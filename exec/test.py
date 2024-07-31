campaign_id = [
    {"campaign_name":"SECOM_P", "url":"https://ads.kwai.com/?accountId=60161580#/index", "ativos": " "},
    {"campaign_name":"teste", "url":"https://ads.kwai.com/?accountId=60161580#/management", "ativos" : " "},
]
for i in range(len(campaign_id)):
    if campaign_id[i]['ativos'] == ' ':
        print(f'A campanha {campaign_id[i]['campaign_name']} ainda não tem o número de ativos selecionado.')
        a = input('Digite o número de ativos desta campanha: ')
        campaign_id[i]['ativos'] = int(a)
    else:
        print(f'A campanha {campaign_id[i]['campaign_name']} já possui {campaign_id[i]['ativos']} ativos adicionados a base do robô.')
print(f'{campaign_id}')

import pyautogui as pg
import time 

pg.press("win")
time.sleep(1)
pg.write("Chrome", interval=0.10)
time.sleep(1)
pg.press("enter")
time.sleep(1)
pg.press("tab")
time.sleep(1)
pg.press("enter")
time.sleep(1)
pg.hotkey('ctrl', 't')
pg.write(f'{campaign_id[0]['url']}', interval=0.10)
pg.press("enter")
time.sleep(30)
i = 0
while i < 7:
    print(f'{i}')
    pg.press("tab")
    time.sleep(0.5)
    i += 1
i = 0
pg.write(f'{campaign_id[0]['campaign_name']}', interval=0.10)
pg.click(x=1234, y=489, clicks=1)
time.sleep(7)

while i < 3:
    print(f'{i}')
    pg.press("tab")
    time.sleep(0.5)
    i += 1    
i = 0
pg.press("enter")

# COLETA DO DADO
# CONFIRMAR VERACIDADE DO DADO

