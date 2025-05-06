import requests
from bs4 import BeautifulSoup

r = requests.get('http://bvbinfo.com/Season.asp?AssocID=3&Year=2025')
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())