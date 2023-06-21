import requests
from bs4 import BeautifulSoup as bs
import json
import re

def extract_repeated_uppercase_words(string_list):
    repeated_uppercase_words = []
    for string in string_list:
        words = re.findall(r'\b([A-Z]{3,})\b', string)
        repeated_uppercase_words.extend(words)
    return repeated_uppercase_words

name_list = []
for pg in range(1,3): # 109,111

    url = f'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EB%8F%99%EC%84%9C%EA%B0%80%EA%B5%AC&pagingIndex={pg}&pagingSize=80&productSet=total&query=%EB%8F%99%EC%84%9C%EA%B0%80%EA%B5%AC' # 52페이지까지 있음.

    req = requests.get(url)

    html = req.text

    cnt = html.count('product_title__Mmw2K')

    print(cnt)
    quit()
    soup = bs(html,'html.parser')

    target_class = "product_title__Mmw2K"

    names = soup.find_all(class_=target_class)
    for name in names:
        print(name.text)
        name_list.append(name.text)

quit()
print(name_list)
print(len(name_list))


with open("ds_109pg.txt", "w") as file:
    for name in name_list:
        file.write(name + "\n")
