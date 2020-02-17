#pip package names: BeautifulSoup4, requests, lxml, html5lib, selenium
#tutorial: https://www.youtube.com/watch?v=ng2o98k983k

from bs4 import BeautifulSoup
import requests
import threading 


def get_data(source_link):

    #Get data from the request
    source = requests.get(source_link).text
    soup = BeautifulSoup(source, 'lxml')
    
    #Get Champion
    champs = soup.find_all('td', class_="champion-icon")
    champList = []
    champs = champs

    for champ in champs:
        champion = str(champ.a.div.img['alt'])
        champList.append(champion)
    
    #Get winning team
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
responses_lock = threading.Lock()
def fetch(links):
    global iterations
    for link in links:
        try:
            data = get_data(link)
            data = data.replace("'","")
            data = data.replace(" ","")
            data = data.replace('"',"")
            data = data.encode("utf-8")
        except:
            print("Failed to fetch data from link: ", link)
        iterations += 1
        with responses_lock:
            responses.append(data)
            print("Link: ", iterations)


#Initialize threads 
threads = []
threadCountTarget = int(input("Number of threads: "))
for i in range(threadCountTarget):
    linksSlice = links[i::threadCountTarget]
    threads.append(threading.Thread(target=fetch, args=(linksSlice, )))
    threads[i].start()

for thread in threads:
    thread.join()


#Log responses to a csv file
csv = open("probuilds_data.csv", "w")
csv.write("BTC1,BTC2,BTC3,BTC4,BTC5,RTC1,RTC2,RTC3,RTC4,RTC5,WIN\n")
for line in responses:
    csv.write(str(line)[2:-1])
    csv.write("\n")
csv.flush()
csv.close()
print("output: probuilds_data.csv")
