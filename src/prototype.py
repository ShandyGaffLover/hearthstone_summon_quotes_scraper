import requests
from bs4 import BeautifulSoup

url = 'https://hearthstone.gamepedia.com/The_Boomsday_Project'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))
