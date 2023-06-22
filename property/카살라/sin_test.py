import requests
from bs4 import BeautifulSoup as bs
import csv
import asyncio
import time
import random

url_list = []
for pg in range(1, 24):
    url = f'https://www.ssg.com/search.ssg?target=all&query=동서카살라&count=100&page={pg}'
    print(f'{pg}/25페이지')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        # 'Authorization': 'Bearer your-access-token'
    }

    req = requests.get(url, verify=False, headers=headers, timeout=10)
    html = req.text
    soup = bs(html, 'html.parser')
    names = soup.find_all(class_='cunit_prod')
    print(type(names))
    for name in names:
        prd_no = name.attrs['data-react-unit-id']
        url = 'https://www.ssg.com/item/itemView.ssg?itemId=' + str(prd_no)
        url_list.append(url)
        print('현재 수집된 상세페이지: ', len(url_list))

    sleep_duration = random.uniform(1, 3)  # Random sleep duration between 1 and 3 seconds
    time.sleep(sleep_duration)

print(len(url_list))
with open('sin_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
    write = csv.writer(f)
    write.writerows([url_list])