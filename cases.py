import requests
from bs4 import BeautifulSoup as bs


url = 'https://www.worldometers.info/coronavirus/'


html = requests.get(url).text
parsed = bs(html, features='lxml').find_all('div', {'class': 'maincounter-number'})

for case, number in zip(['Total cases', 'Death cases', 'Recover cases'], parsed):
    print(case + ':', number.find('span').get_text())
