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


#Load links
print("Opennig 'links.txt'...")
file = open("links.txt", "r")
links = file.read().splitlines() 
responses =[]
iterations = 0

#Make requests
for link in links:
    data = get_data(link)
    data = data.replace("'","")
    data = data.replace(" ","")
    data = data.replace('"',"")
    responses.append(data)
    iterations += 1
    print("Link: ", iterations)

#Log responses to a csv file
csv = open("probuilds_data.csv", "w")
csv.write("BTC1,BTC2,BTC3,BTC4,BTC5,RTC1,RTC2,RTC3,RTC4,RTC5,WIN\n")
for line in responses:
    csv.write(line)
    csv.write("\n")
csv.flush()
csv.close()
print("output: probuilds_data.csv")
