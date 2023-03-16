import requests
#from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import InvalidArgumentException
import time


fireOp = Options()

#fireOp.add_argument("--headless")

HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'}


driver = webdriver.Firefox(options=fireOp)

#

kaupat = {'Skauppa': ("https://www.s-kaupat.fi/tuote/paulig-juhla-mokka-kahvi-suodatinjauhatus-500g/6411300000494", '/html/body/div[1]/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/div/div[1]/span')
,'Tokmanni' : ("https://www.tokmanni.fi/juhla-mokka-500-g-sj-6411300000494", "/html/body/div[3]/main/div[2]/div/div[2]/div[3]/form/div[1]/div[1]/span/span/span"),'Kmarket':("https://www.k-ruoka.fi/kauppa/tuotehaku/juomat/kahvi-ja-suodatinpussit?tuote=juhla-mokka-kahvi-500g-sj-6411300000494", "/html/body/div[1]/div[1]/div/div/div[2]/section/section[1]/div[2]/div[1]/div[2]/div/div[1]/span"),
'HalpaHalli' : ("https://www.halpahalli.fi/juhla-mokka-500g-suodatinjauhettu-kahvi.html", "/html/body/div[3]/main/div[2]/div/div[1]/div[4]/div[1]/span/span/span")}

#del kaupat['Skauppa']

print(len(kaupat))
#kaupat = dict(sorted(kaupat.items()), reversed=True)


time.sleep(2)

for name, data in kaupat.items():
    print(data[0])
    driver.get(data[0])


    hinta = driver.find_element_by_xpath(data[1]).text

    print(f'Kaupan nimi: {name} Kahvin hinta: {hinta}')




driver.quit()




"""
haku = requests.get(Skauppa, headers=HEADERS)

soup = BeautifulSoup(haku.content, 'html.parser')
price = soup.findAll("div", {"class": "price"})
print(price)

"""

