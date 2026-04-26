import requests
import json
url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url)

print(response)

if response.status_code ==200:
    dados_json = response.json()
    print(type(dados_json))

    dados_restaurante ={}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []
        dados_restaurante[nome_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })


else:
    print("Algo deu errado em sua requisição")


for nome_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'OO-Sabor-express\{nome_restaurante}.json'
    print(nome_restaurante,dados,'\n')
    with open (nome_do_arquivo,'w') as arquivo_restaurante:
        json.dump(dados,arquivo_restaurante,indent=4)