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
for pg in range(1,53): # 53

    url = f'https://smartstore.naver.com/dongsuh22/category/cd54f7f9884d4291b8e95de50b533f69?st=POPULAR&dt=LIST&page={pg}&size=80' # 52페이지까지 있음.

    req = requests.get(url)

    html = req.text

    soup = bs(html,'html.parser')

    target_class = "_1Zvjahn0GA"

    names = soup.find_all(class_=target_class)
    for name in names:
        pdt_code = name.text.split(' ')[-1]
        print(pdt_code)
        if not re.search('[가-힣]', pdt_code): # 한글제외
            if 3<len(pdt_code)<=6: # SS/Q와 같이 글자수제한
                pdt = ''.join([p for p in pdt_code if p.isdigit() is False]) #숫자로만 이루어진것 제외
                name_list.append(pdt)
name_list = list(set([n for n in name_list if len(n)>0]))
print(name_list)
print(len(name_list))


with open("name_list.txt", "w") as file:
    for name in name_list:
        file.write(name + "\n")
