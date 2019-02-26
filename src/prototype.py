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


def extract_summon_quotes(href: str) -> str:
    url = 'https://hearthstone.gamepedia.com/' + href
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    tag_written_about_quotes = soup.find('dl')
    try:
        return tag_written_about_quotes.find('dd').find('i').string
    except AttributeError:
        return None
    

expansion_name = 'The_Boomsday_Project'
dict = create_dictionary_of_card_name_and_its_link(expansion_name)
summon_quotes = {}
for card in dict.items():
    summon_quotes[card[0]]=extract_summon_quotes(card[1])
print(summon_quotes.values())
    
