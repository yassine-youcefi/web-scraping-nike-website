import bs4
import json
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

import os 
BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
CSV_FILE = os.path.join(BASE_DIRECTORY, 'data_csv.csv')
JSON_FILE = os.path.join(BASE_DIRECTORY, 'data_json.json')


my_url = {"Chaussures de running" : "https://store.nike.com/fr/fr_fr/pw/homme-v%C3%AAtements/1mdZ7pu?ipp=120",
          "CHAUSSURES DE FOOTBALL" : "https://store.nike.com/fr/fr_fr/pw/homme-compression-nike-pro/7puZobn"}

data_json = []
data_csv = "name_product,discription_product,colors_product,price_product,catégorie\n"

def selection(grides , x):
    global data_csv, data_json
    
    i = 1
    for gride in grides :
        #print('_________/',i,'\________')
        #couleur de produit
        product_colors = gride.div.div.text

        product_info = gride.findAll('div' ,{"class" : "product-name"})
        
        #nom de produit
        product_n = product_info[0].findAll('p' , {"class" : "product-display-name"})
        product_name = product_n[0].text
        
        #discription sur le produit
        product_d = product_info[0].findAll('p' , {"class" : "product-subtitle"})
        product_discription = product_d[0].text
        
        #prix de produit
        product_price1 = gride.findAll('div' ,{"class" : "product-price"})
        product_price2 = product_price1[0].findAll("span" , {"class" : "local"})
        product_price = product_price2[0].text 

        #print(product_name)
        #print(product_discription)
        #print(product_colors)
        #print(product_price)
        
        data_csv = data_csv + "{},{},{},{},{}\n".format (
            product_name, product_discription, product_colors, product_price.replace(',','.'), x
        )
  
        data_json += [{"name" : product_name , "discription" : product_discription , "colors" : product_colors , "price" : product_price}]
        
        # if i < len(grides):
        #     data_csv =  data_csv + ','
        i += 1


if __name__ == '__main__':

    for x in my_url :
        uclient = ureq(my_url[x])
        page_html = uclient.read()
        uclient.close()
        pagesoup = soup(page_html , "html.parser")
        grides = pagesoup.findAll("div" , {"class" : "grid-item-info"})
        print('cotégorie de produits = ', x )
        print('num de produits = ',len(grides))

        selection(grides , x)

    #file save
    with open(CSV_FILE, 'w') as csv_f:
        csv_f.write(data_csv)

    with open(JSON_FILE, 'w') as json_f:
        json_f.write(json.dumps(data_json)+'\n')