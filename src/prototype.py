import requests
from bs4 import BeautifulSoup


def create_dictionary_of_card_name_and_its_link(expansion_name: str) -> dict:
    url = 'https://hearthstone.gamepedia.com/' + expansion_name
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
    return dict



expansion_name = 'The_Boomsday_Project'
dict = create_dictionary_of_card_name_and_its_link(expansion_name)
print(dict.keys())
