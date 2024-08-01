import pyautogui as pg
import time 
import os
import json
from datetime import date

# trazendo os dados
if os.path.exists('config.json'):
    with open('config.json', 'r') as f:
        data = json.load(f)
else:
    print('Não foi possível encontrar os dados de Configuração.')

# entrando no Chrome no perfil selecionado
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

# entrando no site em questão
pg.hotkey('ctrl', 't')
pg.write(f'{data[0]['url']}', interval=0.10)
pg.press("enter")
time.sleep(30)
i = 0
while i < 7:
    pg.press("tab")
    time.sleep(0.5)
    i += 1
i = 0
pg.write(f'{data[0]['id']}', interval=0.10)
pg.click(x=1234, y=489, clicks=1)
time.sleep(7)

# entrada no link de destino final de coleta
pg.hotkey('ctrl', 'l')
pg.press('right')
time.sleep(2)
pg.keyDown('shiftleft')
pg.keyDown('shiftright')
pg.keyDown('ctrl')
pg.press('left')
pg.keyUp('shiftleft')
pg.keyUp('shiftright')
pg.keyUp('ctrl')
pg.press('delete')
time.sleep(2)
pg.write('report/customReport', interval=0.10)
pg.press('enter')
i = 0

while i < 15:
    pg.press("tab")
    time.sleep(0.5)
    if i == 14:
        pg.write(data[0]['startdate'])
        time.sleep(3)
        pg.press('tab')
        time.sleep(0.5)
        pg.press('tab')
        pg.write(f'{date.today()}')
        time.sleep(3)
        pg.press('enter')
        i += 1
    else:
        i +=1
i = 0

while i < 5:
    pg.press("tab")
    time.sleep(0.5)
    if i == 4:
        pg.press('enter')
        time.sleep(2)
        x, y = pg.position()
        pg.click(x, y)
        i += 1
    else:
        i += 1
i = 0
# inicio do processo de coleta



# # entrada nos checks de ativos
# while i < (14 + int(data[0]['ativos'])):
#     pg.press("tab")
#     time.sleep(0.5)
#     if i == 7:
#         pg.write(data[0]['startdate'])
#         pg.press('enter')
#         pg.write(f'{date.today()}')
#         pg.press('enter')
#         time.sleep(3)
#         i += 1
#     elif i in [13 + 2*j for j in range(int(data[0]['ativos']))]:
#         print(f'{i}')
#         pg.press('space')
#         time.sleep(2)
#         i += 1
#     else:
#         i +=1
# i = 0

# # CONFIRMAR VERACIDADE DO DADO

