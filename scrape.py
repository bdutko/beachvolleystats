import requests
from bs4 import BeautifulSoup
import pandas as pd
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)

def get_tourneys(year):
    r = requests.get( f'http://bvbinfo.com/Season.asp?AssocID=3&Year={year}')
    soup = BeautifulSoup(r.content, 'html.parser')
    tournaments =[]
    for result in soup.find_all('a'):
        link = result.get('href')
        if 'Tournament' in link:
            #link = link[link.find('=')+1:]
            link = "http://bvbinfo.com/" + link
            #print(link)
            tournaments.append(link)
    return tournaments

def get_results(linky):
  #  url = 'http://bvbinfo.com/Tournament.asp?ID=4440'
    tr = requests.get( f'{linky}')
    tsoup = BeautifulSoup(tr.content, 'html.parser',from_encoding="utf8", )
    trimsoup = tsoup.find_all('table')
    #print(pd.read_html(tr))
    tbls = pd.read_html(str(tsoup))
    tbl = tbls[3]
    tourneyname = tbl.iloc[0,0]
    tbl = tbl.iloc[1:,:7]
    tbl.reset_index(drop=True, inplace=True)
    tbl.columns = tbl.iloc[0]
    tbl = tbl[1:]
    tbl.reset_index(drop=True,  inplace=True)
    if 'Finish' in tbl.columns:
        tbl[['Finish']] = tbl[['Finish']].apply(pd.to_numeric)
    if 'Points' in tbl.columns:
        tbl[['Points']] = tbl[['Points']].apply(pd.to_numeric)
    #tbl = tbl.values.tolist()
    return tbl

tourneys = get_tourneys(2023)

x = 1
tourneyresults = []
for item in tourneys:
    if x < 999:
        print(x)
        listy = get_results(item).values.tolist()
        tourneyresults = tourneyresults + listy
        #print(get_results(item))
    x = x + 1

res = pd.DataFrame(tourneyresults)
print(res)


res.to_csv('2023_results.csv')

#To-do: add gender differentiation and tourney name