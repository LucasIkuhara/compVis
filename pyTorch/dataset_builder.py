#pip package names: BeautifulSoup4, requests, lxml, html5lib, selenium
#tutorial: https://www.youtube.com/watch?v=ng2o98k983k

from bs4 import BeautifulSoup
import requests


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
    
    champList.append(winner[1:-1])

    return str(champList)[1:-1]


file = open(r"C:\Users\Lucas Ikuhara\Pictures\testzone\pyTorch\links.txt", "r")
links = file.read().splitlines() 

data =[]
for link in links:
    data.append(get_data(link).replace("'",""))

print(data)
csv = open("probuilds_data.csv", "w")
for line in data:
    csv.write(line)
    csv.write("\n")
csv.flush()
csv.close()
print("output: probuilds_data.csv")
