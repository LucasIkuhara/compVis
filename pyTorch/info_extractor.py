#pip package names: BeautifulSoup4, requests, lxml, html5lib
#tutorial: https://www.youtube.com/watch?v=ng2o98k983k

from bs4 import BeautifulSoup
import requests

sourcePage = requests.get("https://www.probuilds.net/").text
soup = BeautifulSoup(sourcePage, 'lxml')

LiveFeed = soup.find('div', id="game-feed") #class_="game-feed pro-history pos-rel") #"game-feed")
links = soup.find_all("a")
print(links)




def get_data(source_link):
    source = requests.get(source_link).text
    soup = BeautifulSoup(source, 'lxml')
    champs = soup.find_all('td', class_="champion-icon")
    champList = []
    champs = champs

    for champ in champs:
        champion = str(champ.a.div.img['alt'])
        champList.append(champion)
    
    winner = soup.find('div', class_="game-details")
    winner = str(winner.p['class'])[:-1:]
    winner = winner[winner.find(" ")+1::]
    
    return (winner, champList)

#print(get_data("https://www.probuilds.net/guide/show/EUW/4337850120/gdWaFhZ7zsJX8psckm35WoTrgZqgXN3tpe9VdRxQUf8WmoY"))
