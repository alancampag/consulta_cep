import requests
import pandas as pd


def search_zip_code(x):
    to_get = ['logradouro', 'bairro', 'localidade', 'uf']
    resp = requests.get(f"https://viacep.com.br/ws/{x['cep']}/json/")
    if resp.status_code == 200:
        for i in to_get:
            x[i] = resp.json()[i]
    return x


df = pd.DataFrame(columns=['cep', 'logradouro', 'bairro', 'localidade', 'uf'])
df['cep'] = pd.read_csv('ceps.csv', sep=';')['cep']
df = df.apply(search_zip_code, axis=1)
df.to_csv('resultados.csv', sep=';', index=False, encoding='utf-8-sig')
