import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
my_url = {"Chaussures de running" : "https://store.nike.com/fr/fr_fr/pw/homme-v%C3%AAtements/1mdZ7pu?ipp=120",
          "CHAUSSURES DE FOOTBALL" : "https://store.nike.com/fr/fr_fr/pw/homme-compression-nike-pro/7puZobn"}
def selection(gride , x):
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
        
        f.write(product_name +' , '+ product_discription +' , '+ product_colors +' , '+ product_price.replace(',','.') + ' , ' + x + '\n')    
        i += 1


if __name__ == '__main__':

    file_name = 'data.csv'
    f = open(file_name , 'w')
    headers = "name_product , discription_product , colors_product , price_product , catégorie\n"
    f.write(headers)

    for x in my_url :
        
        uclient = ureq(my_url[x])
        page_html = uclient.read()
        uclient.close()
        pagesoup = soup(page_html , "html.parser")
        grides = pagesoup.findAll("div" , {"class" : "grid-item-info"})
        print('cotégorie de produits = ', x )
        print('num de produits = ',len(grides))
        gride = grides[0]

        selection(gride , grides , x)
    
    f.close()
        
    