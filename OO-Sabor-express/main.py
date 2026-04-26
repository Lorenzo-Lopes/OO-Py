from fastapi import FastAPI,Query
import requests
import json

app = FastAPI()

@app.get('/api/helloworld')
def hello_Word():
    return{'Hello':'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante:str=Query(None)):

    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
    response = requests.get(url)

    if response.status_code ==200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados':dados_json}
        
        dados_restaurante =[]
        for item in dados_json:
            if item['Company'] == restaurante:

                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return{'Restaunte':restaurante,'Cardapio':dados_restaurante}

    else:
        return{'Erro':f'O Erro foi : {response.status_code} - {response.text}'}