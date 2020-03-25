from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import requests
import csv

def scrap(name):
    path = 'https://www.worldometers.info/coronavirus/country/'
    path = path+name
    path = path+''
    source = requests.get(
        'https://www.worldometers.info/coronavirus/country/').text
    soup = BeautifulSoup(source, 'lxml')
    data = soup.find_all('div', attrs={'id': 'maincounter-wrap'})
    dict = {}
    for i in data:
        s = str(i.span.text)
        dict[(i.h1.text).strip()] = s.strip()
    return dict


print(scrap('brazil'))
