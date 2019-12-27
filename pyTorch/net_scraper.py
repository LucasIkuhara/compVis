from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\Lucas Ikuhara\Pictures\testzone\pyTorch\chromedriver.exe")
driver.get('https://www.probuilds.net/')

for i in range(20):
    load_more = driver.find_element_by_id("moreMatchesButton")
    load_more.click()

sourcePage = requests.get("https://www.probuilds.net/").text
soup = BeautifulSoup(sourcePage, 'lxml')

LiveFeed = soup.find('div', id="game-feed") #class_="game-feed pro-history pos-rel") #"game-feed")
links = soup.find_all("a")
print(links)
