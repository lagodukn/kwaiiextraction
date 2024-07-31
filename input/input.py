import json
import os

if os.path.exists('config.json'):
    with open('config.json', 'r') as f:
        campaign_id = json.load(f)
else:
    campaign_id = [
        {"campaign_name": "SECOM_P", "url": "https://ads.kwai.com/?accountId=60161580#/index", "ativos": " ", "startdate":" ", "enddate":" "},
        {"campaign_name": "teste", "url": "https://ads.kwai.com/?accountId=60161580#/management", "ativos": " ", "startdate":" ", "enddate":" "},
    ]

if not isinstance(campaign_id, list):
    print("Erro: o conteúdo do arquivo config.json é inválido.")
    exit(1)

for i in range(len(campaign_id)):
    if campaign_id[i]['ativos'] == ' ':
        print(f'A campanha {campaign_id[i]["campaign_name"]} ainda não tem o número de ativos selecionado.')
        campaign_id[i]['ativos'] = input('Digite o número de ativos desta campanha: ')
    else:
        print(f'A campanha {campaign_id[i]["campaign_name"]} já possui {campaign_id[i]["ativos"]} ativos adicionados a base do robô.')
add_campaign = input('Deseja adicionar uma nova campanha? (y/n): ')
if add_campaign.lower() == 'y':
    new_campaign_name = input('Digite a palavra-chave da nova campanha: ')
    new_campaign_url = input('Digite a URL da nova campanha somente até #/: ')
    new_campaign_ativos = input('Digite o número de ativos da nova campanha: ')
    campaign_id.append({
        "campaign_name": new_campaign_name,
        "url": new_campaign_url,
        "ativos": int(new_campaign_ativos)
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