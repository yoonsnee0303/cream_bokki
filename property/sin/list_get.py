

import time
import csv
import getpass
path_input = getpass.getuser()


from bs4 import BeautifulSoup as bs




import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
page = 1


all_list = []
while True:
    url = f'https://www.ssg.com/search.ssg?target=all&query=%EC%9E%A5%EC%9D%B8%EA%B0%80%EA%B5%AC%2B%EB%8F%99%EC%84%9C%EA%B0%80%EA%B5%AC&brand=2000020584&count=100&page={page}'
    res = requests.get(url, headers=headers, verify=False)

    ck_end = res.text.count('검색어와 일치하는 상품이 없습니다.')
    if ck_end == 1:
        #list_test csv파일로 저장
        with open('sin_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
            write = csv.writer(f)
            write.writerows([all_list])
        print('수집종료')
        break
    else:
        soup = bs(res.text, 'html.parser')
        elem = soup.find("ul", id="idProductImg")
        elems = elem.find_all("li")
        print(len(elems))

        for el in elems:
            url = el['id'].replace('item_unit_','https://www.ssg.com/item/itemView.ssg?itemId=')
            all_list.append(url)
            print(url)
        page += 1
        time.sleep(3)



