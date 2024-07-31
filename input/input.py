import json
import os
#############################
# data do dia será a end date
from datetime import date
enddate = date.today()
#############################

if os.path.exists('config.json'):
    with open('config.json', 'r') as f:
        campaign_id = json.load(f)
else:
    campaign_id = [
        {"id": "60161580", "ativos": " ", "startdate":" ", "enddate":" "},
        {"id": "60161581", "ativos": " ", "startdate":" ", "enddate":" "},
    ]

if not isinstance(campaign_id, list):
    print("Erro: o conteúdo do arquivo config.json é inválido.")
    exit(1)

for i in range(len(campaign_id)):
    if campaign_id[i]['ativos'] == ' ':
        print(f'A campanha de id {campaign_id[i]["id"]} ainda não tem o número de ativos selecionado.')
        campaign_id[i]['ativos'] = input('Digite o número de ativos desta campanha: ')
    elif campaign_id[i]['startdate'] == ' ':
            print(f'A campanha de id {campaign_id[i]["id"]} ainda não tem data de inicio selecionada.')
            campaign_id[i]['startdate'] = input('Digite a data de inicio da campanha (YYYY-MM-DD): ')
    else:
        print(f'A campanha de id {campaign_id[i]["id"]} já possui {campaign_id[i]["ativos"]} ativos adicionados e {campaign_id[i]["startdate"]} como data de inicio a base do robô.')
                
add_campaign = input('Deseja adicionar uma nova campanha? (y/n): ')
if add_campaign.lower() == 'y':
    new_campaign_id = input('Digite a id da nova campanha: ')
    new_campaign_ativos = input('Digite o número de ativos da nova campanha: ')
    new_campaign_startdate = input('Digite a data de inicio da nova campanha (YYYY-MM-DD)')
    campaign_id.append({
        "id": new_campaign_id,
        "ativos": int(new_campaign_ativos),
        "startdate": new_campaign_startdate
    })
    print(f'Seus novos dados são:\n{campaign_id}')

if os.path.exists('config.json'):
    with open('config.json', 'r') as f:
        old_campaign_id = json.load(f)
    if old_campaign_id != campaign_id:
        with open('config.json', 'w') as f:
            json.dump(campaign_id, f)
else:
    with open('config.json', 'w') as f:
        json.dump(campaign_id, f)