import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.herorealms.com/card-gallery/')
soup = BeautifulSoup(r.text, features='html.parser')
r.close()


for image in soup.find_all('img'):
    r = requests.get(image.get('src'), stream=True)
    path = '.../Cards/' + image.get('src').rsplit('/', 1)[-1]
    if r.status_code == 200:
        with open(path, 'wb') as file:
            file.write(r.content)

print("awd")
