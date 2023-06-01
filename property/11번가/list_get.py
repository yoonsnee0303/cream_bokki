import requests
from bs4 import BeautifulSoup as bs
import csv
import time
import json

json_data = []
detail_url = []
for pg in range(1,9): #41
    url = f'https://search.11st.co.kr/Search.tmall?method=getSearchFilterAjax&kwd=동서가구+장인가구&pageNo={pg}&pageSize=250'
    response = requests.get(url)
    response_json = response.json()  # JSON 형식으로 변환
    for i in range(len(response_json['commonPrdList']['items'])):
        detail_url.append(response_json['commonPrdList']['items'][i]['productDetailUrl'])
    print(len(detail_url))
# print(detail_url)
print(len(set(detail_url)))

with open('11_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
    write = csv.writer(f)
    write.writerows([detail_url])



