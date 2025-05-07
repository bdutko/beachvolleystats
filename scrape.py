import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_tourneys(year):
    r = requests.get( f'http://bvbinfo.com/Season.asp?AssocID=3&Year={year}')
    soup = BeautifulSoup(r.content, 'html.parser')
    tournaments =[]
    for result in soup.find_all('a'):
        link = result.get('href')
        if 'Tournament' in link:
            #link = link[link.find('=')+1:]
            link = "bvbinfo.com/" + link
            #print(link)
            tournaments.append(link)
    return tournaments


#print(get_tourneys(2024))

def get_results():
    tr = requests.get('http://bvbinfo.com/Tournament.asp?ID=4342')
    tsoup = BeautifulSoup(tr.content, 'html.parser')
    trimsoup = tsoup.find_all('table')
    print(trimsoup)
get_results()