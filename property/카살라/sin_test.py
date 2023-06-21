import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.ssg.com/search.ssg?target=all&query=동서카살라&count=100&page=1' #1~23

req = requests.get(url)
html = req.text

print(html)

soup = bs(html,'html.parser')
target_class = 'cunit_t232'
names = soup.find_all(id=target_class)

print(names)
