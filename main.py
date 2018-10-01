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


"""
for image in soup.find_all('img'):
    r = requests.get(image.get('src'), stream=True)
    path = '.../Cards/' + image.get('src').rsplit('/', 1)[-1]
    if r.status_code == 200:
        with open(path, 'wb') as file:
            file.write(r.content)
"""


link = soup.find('td', class_='column-1')
while link.find('img').get('src').rsplit('/', 1)[-1].split('-')[0] == 'BAS':
    images = link.find_all('img')
    for index in range(len(images)):
        FILE.write(images[index].get('src').rsplit('/', 1)[-1])
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

