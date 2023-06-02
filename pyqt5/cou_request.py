import requests
import time
import csv
import math
from bs4 import BeautifulSoup as bs
import json

url = 'https://store.coupang.com/vp/vendors/A00037308/products'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',  # Add the Language header
    # Add more headers as needed
}


result = requests.get(url,headers=headers)
# print(result.text)
# print(result.headers) # 헤더확인
with open('result.txt', 'wb') as file:
    file.write(result.content)
html = result.text
soup = bs(html,"html.parser")
label_tags = soup.find_all('label')
print(label_tags)
tag_list = []
for tag in label_tags:
    if str(tag).__contains__('for="component'):
        parent = tag.parent
        if not str(parent).__contains__('href'):
            tag = str(tag).split(sep='=')[1].split(sep='t')[1].split(sep='"')[0]
            tag_list.append(tag)
print(tag_list)
print(len(tag_list)
