import requests
from bs4 import BeautifulSoup as bs
import json
import time

while True:
    find_word_1 = input("키워드 입력 : ")
    find_word_2 = input("상품명 입력 : ")
    find_word_2 = find_word_2.strip()

    pagingIndex = [pg for pg in range(1,11)]

    for pg in pagingIndex:
        print(f'{pg}','log')
        url = f'https://search.shopping.naver.com/search/all?origQuery={find_word_1}&pagingIndex={pg}&pagingSize=80&productSet=total&query={find_word_1}&sort=rel&timestamp=&viewType=list'

        response = requests.get(url)
        html_content = response.text

        # HTML 파싱
        soup = bs(html_content, 'html.parser')

        # script 태그에서 id가 __NEXT_DATA__인 것 찾기
        target_script = soup.find('script', {'id': '__NEXT_DATA__'})
        try:
            json_data = json.loads(target_script.string)
        except:
            soup = bs(html_content, 'html.parser')
            target_script = soup.find('script', {'id': '__NEXT_DATA__'})
            print('error')
            print('error')            
            print('error')            
            print('error')            

        # # JSON 파일로 저장
        # if target_script:
        #     json_data = json.loads(target_script.string)
        #     with open('test.json', 'w',encoding='utf-8-sig') as f:
        #         json.dump(json_data, f, indent=4, ensure_ascii=False)
        #     print("JSON 파일이 성공적으로 저장되었습니다.")
        # else:
        #     print("해당하는 script 태그를 찾을 수 없습니다.")

        pdt_lists = json_data['props']['pageProps']['initialState']['products']['list']

        stop_log = False
        ad_cnt = 0 # 한 페이지당 광고 개수
        for cnt in range(len(pdt_lists)):
            pdt_item = pdt_lists[cnt]['item']

            # 상품 url
            try:
                pdturl = pdt_item["crUrl"]
                switch = ''
            except:
                if len(pdt_item['adcrUrl']) > 0:
                    switch = 'ad'
                    pdturl = pdt_item["adcrUrl"]
                    ad_cnt +=1
            
            # 상품 순위
            all_rank = pdt_item["rank"]

            # 상품명
            productTitle = pdt_item["productTitle"]

            len1 = find_word_2.split(" ")
            len2 = str(productTitle).split(" ")


            word_count = 0
            for f in range(len(len1)):
                for p in range(len(len2)):
                    if len1[f]==len2[p]:
                        word_count +=1
                        break
            score = int((word_count/len(len1))*100)


            if score > 90:
                if ad_cnt > 5:
                    ad_cnt /= 2
                print(cnt)
                print(ad_cnt)
                print('상품명:',productTitle, score, '%')
                print('전체 상품 순위:',all_rank)
                if cnt < (40+int(ad_cnt)-1):
                    
                    # 전체 페이지 내 순위
                    new_pg = pg*2-1

                    # 한 페이지 내 순위
                    if switch == 'ad':
                        print('ck1')
                        one_page_rank = cnt + 1 
                    else:
                        print('ck2')
                        one_page_rank = cnt + 1 + ad_cnt   # ad_cnt 광고수
                    print(new_pg,'페이지 내에서',one_page_rank,'순위')
                    print(f'광고 개수: {ad_cnt}개')

                    # 네이버쇼핑 url
                    naver_shopping_url = f'https://search.shopping.naver.com/search/all?origQuery={find_word_1}&pagingIndex={new_pg}&pagingSize=40&productSet=total&query={find_word_1}&sort=rel&timestamp=&viewType=list'
                    
                    #  stop stop stop stop stop
                    stop_log = True
                    print('네이버쇼핑 url:',naver_shopping_url)
                    # print('상품 상세페이지 url:',pdturl)
                    break

                else:
                    ad_cnt *= 2
                    
                    # 전체 페이지 내 순위
                    new_pg = pg*2

                    # 한 페이지 내 순위
                    if switch == 'ad':
                        print('ck3')
                        one_page_rank = int(cnt/2) + int(ad_cnt/2)
                    else:
                        print('ck4')
                        one_page_rank = int(cnt+1-40-ad_cnt) # ad_cnt 광고수
                    print(new_pg,'페이지 내에서',one_page_rank,'순위')

                    # 네이버쇼핑 url
                    naver_shopping_url = f'https://search.shopping.naver.com/search/all?origQuery={find_word_1}&pagingIndex={new_pg}&pagingSize=40&productSet=total&query={find_word_1}&sort=rel&timestamp=&viewType=list'
                    
                    # stop stop stop stop stop stop
                    stop_log = True
                    print('네이버쇼핑 url:',naver_shopping_url)
                    # print('상품 상세페이지 url:',pdturl)
                    break
            
        if stop_log == True:
            break
        else:
            print('찾는 상품이 없습니다.')






        



