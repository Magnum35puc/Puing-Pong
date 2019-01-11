import requests
from bs4 import BeautifulSoup

global counter
counter = 1

def getNews():
    global counter
    
    site = requests.get("http://www.lefigaro.fr/flash-actu/")
    soup = BeautifulSoup(site.text.split('class="fig-wg__list-v"')[1], 'html.parser')

    newsList = soup.find_all("a")[4*counter : 4+4*counter]

    toRet = ""

    for i in range(len(newsList)):
        toRet += str(newsList[i]).split('>')[1][:-3].split("\n")[0] + "\n\n"

    counter = (counter+1)%2
    
    return toRet[:-2]
