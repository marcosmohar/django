import requests
from bs4 import BeautifulSoup

def repositories(subject){
    " "
    url = 'https://api.github.com/search/repositories?q=language:{}&sort=stars&order=desc&per_page=10'.format(subject)
    # auth = (<usuario>, <contraseña>)
    r = requests(url,auth)
    rp = list()
    if r.status_code == 200:
        repos = scrapper(r.json()['items'])
        for repo in repos:
            login = repo['owner']['login']
            url = repo['html_url']
            language = repo['language']
            stars = repo['stargazers_count']
            rp.append([login, url, language, stars])
    return rp
}