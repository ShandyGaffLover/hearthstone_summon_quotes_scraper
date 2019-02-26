import requests
from bs4 import BeautifulSoup

url = 'https://hearthstone.gamepedia.com/The_Boomsday_Project'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")

dict = {}
for link in soup.find_all('a'):
    if(link.find('img')==None):
        continue
    title = link.get('title')
    href  = link.get('href')
    if(title != None):
        dict[title] = href
print(dict.keys())
