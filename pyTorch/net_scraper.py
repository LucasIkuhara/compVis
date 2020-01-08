from selenium import webdriver
from bs4 import BeautifulSoup
import time

#driver = webdriver.Chrome(r"C:\Users\Lucas Ikuhara\Pictures\testzone\pyTorch\chromedriver.exe")
#driver.get('https://www.probuilds.net/')

#for i in range(20):
#    load_more = driver.find_element_by_id("moreMatchesButton")
 #   load_more.click()
iterationCounter = 0
interval = 1*60*60

while True:
    sourcePage = requests.get("https://www.probuilds.net/livefeed").text
    soup = BeautifulSoup(sourcePage, 'lxml')

    #Get all matches from 'Live Feed' page
    LiveFeed = soup.find('div', id="game-feed") #class_="game-feed pro-history pos-rel") #"game-feed")
    links = soup.find_all("a")

    #List links we already have
    linksFile = open("links.txt", "r")
    linksInFile = linksFile.readlines()
    linksFile.close()

    #Sort new matches
    linksFile = open("links.txt", "a")
    newLinks = []
    for address in links:
        if address not in linksInFile:
            linksInFile.append(address)
            newLinks.append(address)

    #Add new matches to the txt file
    for address in newLinks:
        linksFile.write(address+"\n")
    linksFile.flush()
    linksFile.close()

    #Iteration control
    iterationCounter +=1
    print("Elapsed runs: ", iterationCounter)
    print("Feel free to close this at any given time. Current iterations are set tp happen every {} hour(s)".format(interval/3600))
