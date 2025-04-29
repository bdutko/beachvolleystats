import requests
r = requests.get('http://bvbinfo.com/Season.asp?AssocID=3&Year=2025')
print(r.content)