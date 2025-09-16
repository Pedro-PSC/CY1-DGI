import requests as r
from bs4 import BeautifulSoup

url = 'https://www.uol.com.br/start/esport/'
page = r.get(url)

s = BeautifulSoup(page.content, 'html.parser')

lista = ['fifa','messi','casimiro','league of legends','pokémon','free fire']

for paragrafo in s.find_all('body'):
    for palavra in lista:
        for palavra_str in paragrafo.stripped_strings:
            if palavra.upper() in str(palavra_str).upper():
                print(f'NOTÍCIA SOBRE: {palavra.upper()}\n{palavra_str}')
                break