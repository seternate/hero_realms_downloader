import requests, re
from bs4 import BeautifulSoup
import os


def create_path(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


create_path('Cards/')
PATH = 'Cards/' + 'data.txt'
FILE = open(PATH, 'w', encoding='utf-8')


r = requests.get('https://www.herorealms.com/card-gallery/')
soup = BeautifulSoup(r.text, features='html.parser')
r.close()
for breaks in soup.find_all('br'):
    breaks.extract()
for breaks in soup.find_all('hr'):
    breaks.extract()


link = soup.find('td', class_='column-1')
while link.find('img').get('src').rsplit('/', 1)[-1].split('-')[0] == 'BAS':
    images = link.find_all('img')
    for index in range(len(images)):
        FILE.write(images[index].get('src').rsplit('/', 1)[-1])
        r = requests.get(images[index].get('src'), stream=True)
        with open('Cards/' + images[index].get('src').rsplit('/', 1)[-1], 'wb') as f:
            f.write(r.content)
        if index is not len(images)-1:
            FILE.write(',')
    FILE.write(';')

    for index in range(2):
        link = link.find_next('td')
        FILE.write(link.string if link.string is not None else 'None')
        FILE.write(';')

    link = link.find_next('td')
    text = " ".join(link.renderContents().decode('utf-8').split())
    FILE.write(text if text is not '' else 'None')
    FILE.write(';')

    for index in range(6):
        link = link.find_next('td')
        FILE.write(link.string if link.string is not None else 'None')
        FILE.write(';')

    link = link.find_next('td')
    FILE.write(link.string if link.string is not None else 'None')
    FILE.write('\n')
    link = link.find_next('td')


FILE.close()

