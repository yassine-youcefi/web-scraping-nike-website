import bs4
import json
import requests

from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup


import os
BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
CSV_FILE = os.path.join(BASE_DIRECTORY, 'data_csv.csv')
JSON_FILE = os.path.join(BASE_DIRECTORY, 'data_json.json')


my_url = {"Chaussures de foot": "https://www.nike.com/ma/en/w/mens-football-shoes-1gdj0znik1zy7ok"}

data_json = []
data_csv = "name_product,discription_product,colors_product,price_product,catégorie\n"


def selection(grides, x):
    global data_csv, data_json

    i = 1
    for gride in grides:
        # print('_________/',i,'\________')
        # couleur de produit
        product_colors = gride.findAll(
            'div', {"class": "product-card__product-count"})

        print("products color", product_colors[0].text)

        product_info = gride.findAll(
            'div', {"class": "product-card__title"})

        print("products infos", product_info[0].text)

        # nom de produit
        product_n = product_info[0].findAll(
            'p', {"class": "product-card__titles"})
        print('product-n', product_n)

        product_name = product_n[0].text

        print('product dispaly name ', product_name)

        # discription sur le produit
        product_d = product_info[0].findAll('p', {"class": "product-subtitle"})
        product_discription = product_d[0].text

        # prix de produit
        product_price1 = gride.findAll('div', {"class": "product-price"})
        product_price2 = product_price1[0].findAll("span", {"class": "local"})
        product_price = product_price2[0].text

        # print(product_name)
        # print(product_discription)
        # print(product_colors)
        # print(product_price)

        data_csv = data_csv + "{},{},{},{},{}\n".format(
            product_name, product_discription, product_colors, product_price.replace(
                ',', '.'), x
        )

        data_json += [{"name": product_name, "discription": product_discription,
                       "colors": product_colors, "price": product_price}]

        # if i < len(grides):
        #     data_csv =  data_csv + ','
        i += 1


if __name__ == '__main__':

    for x in my_url:
        uclient = requests.get(my_url[x])
        # page_html = uclient.read()
        # uclient.close()
        soup2 = soup(uclient.text, 'html.parser')

        print('-----------', uclient)
        pagesoup = soup(uclient.text, "html.parser")
        grides = pagesoup.findAll(
            "div", {"class": "product-card__body"})

        print('cotégorie de produits = ', x)
        print('num de produits = ', len(grides))

        selection(grides, x)

    # file save
    with open(CSV_FILE, 'w') as csv_f:
        csv_f.write(data_csv)

    with open(JSON_FILE, 'w') as json_f:
        json_f.write(json.dumps(data_json)+'\n')
