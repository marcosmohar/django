import requests
from bs4 import BeautifulSoup

def medium_articles(subject):
    # establecer la url base
    url = 'https://medium.com/tag/{}/latest'.format(subject)
    # usar requests para "jalar" la url
    r = requests.get(url)
    # parsear el texto de la respuesta con beautiful soup
    soup = BeautifulSoup(r.text, 'html.parser')
    # scrapear los pedazos que queremos de la sopa
    items = soup.find_all('div', 'streamItem')
    # títulos
    h3 = soup.find_all('h3')
    
    readMore = soup.find_all(attrs = {"class":'postArticle-readMore'})
    readMore_links = list()
    for rm in readMore:
        readMore_links.append(rm.a.get('href').split('?')[0])
    
    
    def append_title(item):
        return item.text


    # link = readMore[1].a.get('href').split('?')[0]