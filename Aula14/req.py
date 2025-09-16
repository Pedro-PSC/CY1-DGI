import requests as r
from bs4 import BeautifulSoup

try:
    resultado = r.get('https://www.uol.com.br')
except Exception as erro:
    print(f'Erro: {erro}')
else:
    resposta = resultado.text
    s = BeautifulSoup(resposta, 'html.parser')

    print(s.title.string)
    print(s.h1['class'])
    print(s.find("h2", class_='kicker kicker--live headlineHorizontalLive__content__kicker').prettify())