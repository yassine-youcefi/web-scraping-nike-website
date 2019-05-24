from bs4 import BeautifulSoup
import requests,hashlib

url = 'https://store.nike.com/fr/fr_fr/pw/homme-running-chaussures/7puZ8yzZoi3'


def getNikeData(url,category=None):
        nikePage = requests.get(url)
        nikeData = []
        listUrl = []
        soup = BeautifulSoup(nikePage.content, 'html.parser')
        # find number of articles 
        nbr = soup.select('span.nsg-text--medium-light-grey')[0].getText()
        nbr = nbr.replace('(','')
        nbr = nbr.replace(')','')
        #request with url of all article
        nikePage = requests.get(url+'?ipp='+nbr)
        soup = BeautifulSoup(nikePage.content, 'html.parser')
        articles = soup.find_all('div',{'class':'grid-item-info'})
        urls = soup.find_all('div',{'class':'grid-item-image'})
        for u in urls:
                #(u.select('a')[0]['href'].split('pour-'))[1].split(' ')[0]
                listUrl.append(u.select('a')[0]['href'])
        #get data of article from articles
        for article in articles:
                color = article.select('div.number-of-colors')
                productName = article.select('p.product-display-name')
                price = article.select('span.local')
                discription = article.select('p.product-subtitle')
                #put data into list nikeData if productName not null
                if productName and color and price and discription:
                        nikeData.append({"productId":"","productName":productName[0].getText(),"discription":discription[0].getText(),"colorNumber":color[0].getText(),"price":price[0].getText(),"category":category})
        
        for index in range(0,len(nikeData)):
              nikeData[index]["productId"] = str(int(hashlib.md5(listUrl[index].encode('utf-8')).hexdigest(), 16))[:10]
        return nikeData
getNikeData('https://store.nike.com/fr/fr_fr/pw/homme-running-chaussures/7puZ8yzZoi3')