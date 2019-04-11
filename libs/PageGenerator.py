import requests
from bs4 import BeautifulSoup
# import sys

def generate_page (url, name):
    url, name = url, name

    response = requests.get (url)
    soup = BeautifulSoup (response.content, 'html.parser')

    form = soup.find ('form')
    form ['action'] = '/'

    # for form in soup.find('form'):
        # if len(form['action']) == 0:
            # form ['action'] = '/'
        # elif 'login' in form ['action']:
            # form ['action'] = '/'
    # 

    with open (f'./templates/{name}', 'wt') as file:
        file.write (soup.prettify())

    return True
