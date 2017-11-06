import requests
from bs4 import BeautifulSoup

def medium_articles(subject):

    url = 'https://medium.com/tag/{}/latest'.format(subject)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.find_all('div', 'streamItem')
    readMore = soup.find_all(attrs = {"class":'postArticle-readMore'})
    # link = readMore[1].a.get('href').split('?')[0]