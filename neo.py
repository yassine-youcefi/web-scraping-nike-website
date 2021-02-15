#!/usr/bin/python
# -*- coding: latin-1 -*-
import requests
import json
import os
from bs4 import BeautifulSoup

#pip install virtualenv
#source venv/bin/activate
#pip3 install -r requirements.txt

url = 'https://www.ouedkniss.com/store/?id=2537'

BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
CSV_FILE = os.path.join(BASE_DIRECTORY, 'data_csv.csv')
JSON_FILE = os.path.join(BASE_DIRECTORY, 'data_json.json')
STORE_URLS = os.path.join(BASE_DIRECTORY, 'store_urls.json')

data_json = []
store_url = []
data_csv = "titre, vue, quartie, pieces, etage, description, superficie, prix, numero\n"


def getStorUrls(my_url):
    global store_url
    req = requests.get(my_url)
    soup = BeautifulSoup(req.text, 'html.parser')
    grides = soup.findAll("li", {"class": "produit_titre"})
    l = []

    for gride in grides:
        link = gride.a.get('href')
        proto = "https://www.ouedkniss.com/"
        link = proto + link
        store_url +=[{"url":link}+'\n']
        l.append(link)
    


getStorUrls(url)
print("store url  \n",store_url)

with open(STORE_URLS, 'w') as json_f:
    json_f.write(json.dumps(store_url)+'\n')

# for i in range(len(k)):
#     print("k[i] =\n",k[i])

#     req2 = requests.get(k[i])

# l = "https://www.ouedkniss.com/vente-appartement-f2-alger-centre-algerie-immobilier-d24540614?"
# req2 = requests.get(l)
# soup2 = BeautifulSoup(req2.text, 'html.parser')

# # extrai nom d'article
# article_titre = soup2.h1.text
# print(article_titre)
# container = soup2.find("div", {"id": "Description"})


# # extrai nombre de vues
# disc = container.findAll('span', {"class": "description_span"})
# nombre_vue = disc[1].text
# print(nombre_vue)

# date = disc[2].text.encode('utf-8').strip()
# print(date)

# # extrait quartier
# quart = container.find('p', {"id": "Quartier"})
# quartie = quart.span.text
# print(quartie)

# # extrait nombre des piéces
# nb = container.find('p', {"id": "Nombre de pièces"})
# nombre_piece = nb.span.text
# print(nombre_piece)

# # extrait nombre d'etage
# nbe = container.find('p', {"id": "Nombre d"})
# nombre_etage = nbe.span.text
# print(nombre_etage)

# # description
# descri = container.find('div', {"id": "GetDescription"})
# description = descri.text.encode('utf-8').strip()
# print(description)

# # Superficie
# sup = container.find('p', {"id": "Superficie"})
# superficie = sup.span.text.encode('utf-8').strip()
# print(superficie)

# # prix
# pr = soup2.find("div", {"id": "espace_prix"})
# prix = pr.p.span.text.encode('utf-8').strip()
# print(prix)

# # membre_562700
# num = soup2.find("div", {"id": "membre_562700"})
# numero = num.p.a.text
# print(numero)

# # save data
# data_csv = data_csv + "{},{},{},{},{},{},{},{},{}\n".format(
#     article_titre, nombre_vue, quartie, nombre_piece, nombre_etage, description, superficie, prix, numero.replace(
#         ',', '.'),
# )

# data_json += [{"titre": article_titre,
#                "vues": nombre_vue,
#                "quartie": quartie,
#                "pieces": nombre_piece,
#                "etage": nombre_etage,
#                "descreptio": description,
#                "superficier": superficie,
#                "prix": prix,
#                "tel": numero}]

# # save in files
# with open(CSV_FILE, 'w') as csv_f:
#     csv_f.write(data_csv)

# with open(JSON_FILE, 'w') as json_f:
#     json_f.write(json.dumps(data_json)+'\n')

