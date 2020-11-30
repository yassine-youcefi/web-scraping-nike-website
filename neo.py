import requests
from bs4 import BeautifulSoup

my_url = 'https://www.ouedkniss.com/store/?id=2537'

req = requests.get(my_url)
soup = BeautifulSoup(req.text, 'html.parser')
grides = soup.findAll("li", {"class": "produit_titre"})
l = []

for gride in grides:
    link = gride.a.get('href')
    proto = "https://www.ouedkniss.com/"
    link = proto + link
    l.append(link)

print(l[0])
req2 = requests.get(l[0])
soup2 = BeautifulSoup(req2.text, 'html.parser')

# extrai nom d'article
article_titre = soup2.h1.text
container = soup2.find("div", {"id": "Description"})

# extrai nombre de vues
disc = container.findAll('span', {"class": "description_span"})
nombre_vue = disc[1].text
print(nombre_vue)

date = disc[2].text.encode('utf-8').strip()
print(date)

quart = container.find('p', {"id": "Quartier"})
quartie = quart.span.text
print(quartie)
