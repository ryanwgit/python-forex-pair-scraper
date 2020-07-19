import bs4
import requests
from bs4 import BeautifulSoup
import time

def parsePrice():
    r=requests.get('https://finance.yahoo.com/quote/USDJPY=x')
    soup=bs4.BeautifulSoup(r.text, "html.parser")
    price=soup.findAll('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

while True:
    print('USD/JPY: $' +str(parsePrice()))
    time.sleep(5)

