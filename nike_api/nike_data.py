from bs4 import BeautifulSoup
import requests

url = 'https://store.nike.com/fr/fr_fr/pw/homme-running-chaussures/7puZ8yzZoi3'


def getNikeData(url):
        nikePage = requests.get(url)
        nikeData = []
        soup = BeautifulSoup(nikePage.content, 'html.parser')
        # find number of articles 
        nbr = soup.select('span.nsg-text--medium-light-grey')[0].getText()
        nbr = nbr.replace('(','')
        nbr = nbr.replace(')','')
        #request with url of all article
        nikePage = requests.get(url+'?ipp='+nbr)
        soup = BeautifulSoup(nikePage.content, 'html.parser')
        articles = soup.find_all('div',{'class':'grid-item-info'})
        #get data of article from articles
        for article in articles:
                color = article.select('div.number-of-colors')
                productName = article.select('p.product-display-name')
                price = article.select('span.local')
                discription = article.select('p.product-subtitle')
                #put data into list nikeData if productName not null
                if productName and color and price and discription:
                        nikeData.append({"productName":productName[0].getText(),"discription":discription[0].getText(),"colorNumber":color[0].getText(),"price":price[0].getText()})
        return nikeData





