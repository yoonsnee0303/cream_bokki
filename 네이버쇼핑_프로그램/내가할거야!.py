'''
page 상단 : page가 홀수이면 상단 : n, n+1, n+2, n+3 ... n+9
page 하단 : page가 짝수이면 하단 : 2n
'''

'''
rank는 4구획으로 나눔.
3
---
20
20
----
3
---
20
20

광고/ 광고 없음 나눌 예정.
'''

import requests
from bs4 import BeautifulSoup as bs
import json
import time

find_word_1 = input("키워드 입력 : ")
find_word_2 = input("상품명 입력 : ")
find_word_2 = find_word_2.strip()

pagingIndex = [page for page in range(1,11)] # 80개 상품 기준으로 1~10페이지까지. 총 800개상품

for page in pagingIndex:
    print(f'{page}','log')
    url = f'https://search.shopping.naver.com/search/all?origQuery={find_word_1}&pagingIndex={page}&pagingSize=80&productSet=total&query={find_word_1}&sort=rel&timestamp=&viewType=list'

    response = requests.get(url)
    html_content = response.text

    # HTML 파싱
    soup = bs(html_content, 'html.parser')

    target_script = soup.find('script', {'id': '__NEXT_DATA__'})
    json_data = json.loads(target_script.string)
    pdt_lists = json_data['props']['pageProps']['initialState']['products']['list']
    
    print(len(pdt_lists))

    for pdt_cnt in range(len(pdt_lists)): 
        pdt_item = pdt_lists[pdt_cnt]['item']


        if pdt_cnt<3:
            check = 'ad' 
            
        elif 2< pdt_cnt< 43:
            check = '상단상품'
        
        elif 42< pdt_cnt < 46:
            check = 'ad'

        elif 45 < pdt_cnt:
            check = '하단상품'    


        # 상품명
        productTitle = pdt_item[productTitle]

        len1 = find_word_2.split(" ")
        len2 = str(productTitle).split(" ") 

        # 일치 확인
        word_count = 0
        for f in range(len(len1)):
            for p in range(len(len2)):
                if len1[f]==len2[p]:
                    word_count +=1
                    break
        score = int((word_count/len(len1))*100)      

        
        
