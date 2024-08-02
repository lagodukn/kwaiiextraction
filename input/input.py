import json
import os
#############################
# data do dia será a end date
from datetime import date
enddate = date.today()
#############################

## transformar isto em uma função de checagem se existe o config.json (transformar em dado de banco?)
if os.path.exists('config.json'):
    with open('config.json', 'r') as f:
        data = json.load(f)
else:
    data = [
        {"url":"https://ads.kwai.com/?accountId=60161580#/index","id": "60161580", "ativos": " ", "startdate":" ", "enddate":" "},    
    ]

if not isinstance(data, list):
    print("Erro: o conteúdo do arquivo config.json é inválido.")
    exit(1)

## transformar isto em uma função que gera um popup com inputfield para preenhimento de dados para fins de cadastro de um
## novo item no config.json e checagem de existência de dados para ter uma presença dos dados por inteiro.
for i in range(len(data)):
    if data[i]['ativos'] == ' ':
        print(f'A campanha de id {data[i]["id"]} ainda não tem o número de ativos selecionado.')
        data[i]['ativos'] = input('Digite o número de ativos desta campanha: ')
    elif data[i]['startdate'] == ' ':
            print(f'A campanha de id {data[i]["id"]} ainda não tem data de inicio selecionada.')
            data[i]['startdate'] = input('Digite a data de inicio da campanha (YYYY-MM-DD): ')
    else:
        print(f'A campanha de id {data[i]["id"]} já possui {data[i]["ativos"]} ativos adicionados e {data[i]["startdate"]} como data de inicio a base do robô.')
                
add_campaign = input('Deseja adicionar uma nova campanha? (y/n): ')
if add_campaign.lower() == 'y':
    new_campaign_url = data[0]['url']
    new_campaign_id = input('Digite a id da nova campanha: ')
    new_campaign_ativos = input('Digite o número de ativos da nova campanha: ')
    new_campaign_startdate = input('Digite a data de inicio da nova campanha (YYYY-MM-DD)')
    data.append({
        "url": new_campaign_url,
        "id": new_campaign_id,
        "ativos": int(new_campaign_ativos),
        "startdate": new_campaign_startdate
    })
    print(f'Seus novos dados são:\n{data}')

if os.path.exists('config.json'):
    with open('config.json', 'r') as f:
        old_campaign_id = json.load(f)
    if old_campaign_id != data:
        with open('config.json', 'w') as f:
            json.dump(data, f)
else:
    with open('config.json', 'w') as f:
        json.dump(data, f)