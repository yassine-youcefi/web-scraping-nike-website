import bs4
import json
import requests

from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup


import os
BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
CSV_FILE = os.path.join(BASE_DIRECTORY, 'data_csv.csv')
JSON_FILE = os.path.join(BASE_DIRECTORY, 'data_json.json')

data_json = []
data_csv = "name_product,discription_product,colors_product,price_product,catégorie\n"


my_url = {}
url = ["https://www.nike.com/ma/en/w/mens-football-shoes-1gdj0znik1zy7ok",
       "https://www.nike.com/ma/en/w/mens-jordan-shoes-37eefznik1zy7ok"]


def urls(url):
    global my_url
    for u in url:
        cat = requests.get(u)
        soup2 = soup(cat.text, 'html.parser')

        categorie_soup = soup2.findAll(
            "h1", {"class": "wall-header__title css-hrsjq4 css-7m6ucd css-yj4gxb"})
        categorie = categorie_soup[0].text
        my_url.update({categorie: u})
    print('my_url ', my_url)


def selection(grides, x):
    global data_csv, data_json

    i = 1
    try:
        for gride in grides:
            # print('_________/',i,'\________')
            # couleur de produit
            product_c = gride.findAll(
                'div', {"class": "product-card__product-count"})

            product_colors = product_c[0].text
            print("products color", product_c[0].text)

            try:
                # nom de produit
                product_n = gride.findAll(
                    'div', {"class": "product-card__titles"})

                product_name = product_n[0].text
                print('product name ', product_name)

                # discription sur le produit
                product_d = gride.findAll(
                    'div', {"class": "product-card__subtitle"})
                product_discription = product_d[0].text

                print("discription ", product_discription)
                # prix de produit

                product_price1 = gride.findAll(
                    'div', {"class": "product-price css-11s12ax is--current-price"})
                product_price = product_price1[0].text

                # print(product_name)
                # print(product_discription)
                # print(product_colors)
                print("price ", product_price)

            except:
                product_name = ""
                product_price = ""
                product_discription = ""

            data_csv = data_csv + "{},{},{},{},{}\n".format(
                product_name, product_discription, product_colors, product_price.replace(
                    ',', '.'), x
            )
            data_json += [{"name": product_name, "discription": product_discription,
                           "colors": product_colors, "price": product_price}]
            i += 1
    except:
        print('ERROR')


if __name__ == '__main__':

    # for x in my_url:
    #     uclient = requests.get(my_url[x])
    #     soup2 = soup(uclient.text, 'html.parser')

    #     pagesoup = soup(uclient.text, "html.parser")
    #     grides = pagesoup.findAll(
    #         "div", {"class": "product-card__body"})

    #     print('cotégorie de produits = ', x)
    #     print('num de produits = ', len(grides))

    #     selection(grides, x)

    # # file save
    # with open(CSV_FILE, 'w') as csv_f:
    #     csv_f.write(data_csv)

    # with open(JSON_FILE, 'w') as json_f:
    #     json_f.write(json.dumps(data_json)+'\n')
    urls(url)
