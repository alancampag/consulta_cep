import requests
import pandas as pd


def search_zip_code(x):
    to_get = ['logradouro', 'bairro', 'localidade', 'uf']
    x['cep'] = x['cep'].zfill(8)
    resp = requests.get(f"https://viacep.com.br/ws/{x['cep']}/json/")
    print(f"Buscando {x['cep']}")
    if resp.status_code == 200:
        print('erro' if 'erro' in list(resp.json().keys()) else 'sucesso')
        if 'erro' not in list(resp.json().keys()):
            for i in to_get:
                x[i] = resp.json()[i]
    else:
        print('erro')
    return x


df = pd.DataFrame(columns=['cep', 'logradouro', 'bairro', 'localidade', 'uf'])
df['cep'] = pd.read_csv('ceps.csv', sep=';', dtype='string')['cep']
df = df.apply(search_zip_code, axis=1)
df.to_csv('resultados.csv', sep=';', index=False, encoding='utf-8-sig')

input("Pressione qualquer tecla para fechar")
