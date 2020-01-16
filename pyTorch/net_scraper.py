from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests

n = int(int(input("How many games should be fetched (Approx): "))/10)
maxFailedAttempts = int(input("Fail tolerance: "))

#Driver declaration
driver = webdriver.Chrome(r"C:\Users\Lucas Ikuhara\Pictures\testzone\pyTorch\chromedriver.exe")
driver.get('https://www.probuilds.net/')

#Hit 'View More' button
failedAttempts = 0
for i in range(n):
    if failedAttempts > maxFailedAttempts:
        break
    try:
        load_more = driver.find_element_by_id("moreMatchesButton")
        load_more.click()
        time.sleep(3)
    except:
        time.sleep(5)
        failedAttempts += 1
        continue
        
#Get source page from the Selenium Driver
sourcePage = driver.page_source
soup = BeautifulSoup(sourcePage, 'lxml')
soup = soup.find("div", class_='game-feed pro-history pos-rel')

#Get all matches from 'Live Feed' page
LiveFeed = soup.find('div', id="game-feed") #class_="game-feed pro-history pos-rel") #"game-feed")
elements = soup.find_all("a")
links = []
for element in elements:
    links.append("https://www.probuilds.net" + element["href"])

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

driver.quit()
print("Done fetching data")
