import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url = "https://store.nike.com/fr/fr_fr/pw/homme-compression-nike-pro/7puZobn"

uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html , "html.parser")

grides = page_soup.findAll("div" , {"class" : "grid-item-info"})
len(grides)
gride = grides[0]

i = 1
for gride in grides :
    print('_____',i,'________')
    #couleur de produit
    product_colors = gride.div.div.text

    product_info = gride.findAll('div' ,{"class" : "product-name"})
    
    #nom de produit
    product_n = product_info[0].findAll('p' , {"class" : "product-display-name nsg-font-family--base edf-font-size--regular nsg-text--dark-grey"})
    product_name = product_n[0].text
    
    #discription sur le produit
    product_d = product_info[0].findAll('p' , {"class" : "product-subtitle nsg-font-family--base edf-font-size--regular nsg-text--medium-grey"})
    product_discription = product_d[0].text
    
    print('name = ' + product_name)
    print('discription = ' + product_discription)
    print('couleure = ' + product_colors)

    #prix de produit
    product_price1 = gride.findAll('div' ,{"class" : "product-price edf-font-size--regular nsg-text--medium-grey"})
    if len(product_price1) > 0 :  
        product_price2 = product_price1[0].findAll("span" , {"class" : "local nsg-font-family--base"})
        product_price = product_price2[0].text 
        i += 1
        print('prix = ' + product_price)