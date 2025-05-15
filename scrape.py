import requests
from bs4 import BeautifulSoup
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

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
    url = 'http://bvbinfo.com/Tournament.asp?ID=4342'
    tr = requests.get(url)
    tsoup = BeautifulSoup(tr.content, 'html.parser',from_encoding="utf8", )
    trimsoup = tsoup.find_all('table')
   # print(pd.read_html(tr))
    tbls = pd.read_html(str(tsoup))
    tbl = tbls[3]
    tbl = tbl.iloc[:,:7]
    return tbl
    
print(get_results())