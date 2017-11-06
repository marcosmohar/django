import requests
from bs4 import BeautifulSoup
from .models import Repositories

def repositories(subject){
    " "
    url = 'https://api.github.com/search/repositories?q=language:{}&sort=stars&order=desc&per_page=10'.format(subject)
    # auth = (<usuario>, <contraseña>)
    r = requests(url,auth)
    rp = list()
    if r.status_code == 200:
        repos = scrapper(r.json()['items'])
        for repo in repos:
            Repositories.objects.create(
            owner = repo['owner']['login']
            url = repo['html_url']
            language = repo['language']
            stars = int(repo['stargazers_count'])
            )
}