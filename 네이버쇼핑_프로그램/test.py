import requests
from bs4 import BeautifulSoup as bs
import json
import time

while True:
    find_word_1 = input("키워드 입력 : ")
    find_word_2 = input("상품명 입력 : ")
    find_word_2 = find_word_2.strip()

    pagingIndex = [pg for pg in range(1,11)] # 80개 상품을 기준으로 1~10pg 총 800개 상품

    for pg in pagingIndex:
        print(f'{pg}','log')
        url = f'https://search.shopping.naver.com/search/all?origQuery={find_word_1}&pagingIndex={pg}&pagingSize=80&productSet=total&query={find_word_1}&sort=rel&timestamp=&viewType=list'

        response = requests.get(url)
        html_content = response.text

        # HTML 파싱
        soup = bs(html_content, 'html.parser')

        # script 태그에서 id가 __NEXT_DATA__인 것 찾기
        target_script = soup.find('script', {'id': '__NEXT_DATA__'})
        json_data = json.loads(target_script.string)

        # JSON 파일로 저장
        if target_script:
            json_data = json.loads(target_script.string)
            with open('test.json', 'w',encoding='utf-8-sig') as f:
                json.dump(json_data, f, indent=4, ensure_ascii=False)
            print("JSON 파일이 성공적으로 저장되었습니다.")
        else:
            print("해당하는 script 태그를 찾을 수 없습니다.")

        pdt_lists = json_data['props']['pageProps']['initialState']['products']['list']
        ad_cnt = len(pdt_lists) - 80 # 광고개수

        stop_log = False
        for cnt in range(len(pdt_lists)):
            pdt_item = pdt_lists[cnt]['item']
            
            # 상품 url
            try:
                pdturl = pdt_item["crUrl"]
                status = ''
            except:
                pdturl = pdt_item["adcrUrl"]
                status = 'ad'
            # 상품 순위
            all_rank = pdt_item["rank"]

            # 상품명
            productTitle = pdt_item["productTitle"]

            # 일치하는지 확인
            len1 = find_word_2.split(" ")
            len2 = str(productTitle).split(" ")

            word_count = 0
            for f in range(len(len1)):
                for p in range(len(len2)):
                    if len1[f]==len2[p]:
                        word_count +=1
                        break
            score = int((word_count/len(len1))*100)

            correct_word_list = []
            if score > 90: # 확률이 90프로 이상          
                print('상품명:',productTitle, score, '%')
                print('전체 상품 순위:',all_rank) #####?광고 전체 상품 순위가 제대로 출력되지 않음?

                # 40 페이지 상단(0~43)
                if cnt < (40+ad_cnt):
                    print('ck1')
                    print(cnt)

                    # PAGE
                    new_pg = pg

                    # Rank
                    # 광고일 경우
                    if status == 'ad':
                        print('ck2')
                        one_page_rank = cnt + 1 
                        if cnt > 23: # 40페이지를 기준으로 중간광고
                            one_page_rank = cnt + 1 - 20 
                        print(new_pg,'페이지 내에서',one_page_rank,'순위')
                    else:
                        print('ck3')
                        one_page_rank = cnt + 1 -3 # - int(ad_cnt/2) # ad_cnt 광고수
                        print(new_pg,'페이지 내에서',one_page_rank,'순위') 



                    # 네이버쇼핑 url
                    naver_shopping_url = f'https://search.shopping.naver.com/search/all?origQuery={find_word_1}&pagingIndex={new_pg}&pagingSize=40&productSet=total&query={find_word_1}&sort=rel&timestamp=&viewType=list'

                    print('네이버쇼핑 url:',naver_shopping_url)
                    stop_log = True
                    correct_word_list.append([{'상품명':f'{productTitle}','전체 상품 순위':f'{all_rank}','페이지':f'{new_pg}','순위':f'{one_page_rank}','url':{naver_shopping_url}}])
                    # print('상품 상세페이지 url:',pdturl)
                    break
                
                # 40 페이지 하단(43~)
                # elif (20+ad_cnt/2) < cnt < (20+ad_cnt):
                #     print('ck4')

                #     # 페이지
                #     new_pg = pg*2-1

                #     # 한 페이지 내에서의 랭크
                #     if status == 'ad':
                #         print('ck5')
                #         one_page_rank = cnt + 1
                #         print(new_pg,'페이지 내에서',one_page_rank,'순위')
                #     else:
                #         print('ck6')
                #         one_page_rank = cnt + 1 - int(ad_cnt/2) # ad_cnt 광고수
                #         print(new_pg,'페이지 내에서',one_page_rank,'순위')

                #     # 네이버쇼핑 url
                #     naver_shopping_url = f'https://search.shopping.naver.com/search/all?origQuery={find_word_1}&pagingIndex={new_pg}&pagingSize=40&productSet=total&query={find_word_1}&sort=rel&timestamp=&viewType=list'

                #     print('네이버쇼핑 url:',naver_shopping_url)
                #     stop_log = True
                #     correct_word_list.append([{'상품명':f'{productTitle}','전체 상품 순위':f'{all_rank}','페이지':f'{new_pg}','순위':f'{one_page_rank}','url':{naver_shopping_url}}])
                #     # print('상품 상세페이지 url:',pdturl)
                #     break

                
                # 페이지 하단
                else:
                    print('ck5')
                    print(cnt)
                    print(pg)
                    time.sleep(1000)

                    # 페이지
                    new_pg = pg*2

                    # if status == 'ad':
                    #     print('ck6')
                    #     one_page_rank = cnt + 1 
                    #     if cnt > 23: # 40페이지를 기준으로 중간광고
                    #         one_page_rank = cnt + 1 - 20 
                    #     print(new_pg,'페이지 내에서',one_page_rank,'순위')
                    # else:
                    #     print('ck7')
                    #     one_page_rank = cnt + int(ad_cnt/2) + 1 # - int(ad_cnt/2) # ad_cnt 광고수
                    #     print(new_pg,'페이지 내에서',one_page_rank,'순위') 

                    # 한 페이지 내에서의 랭크
                    one_page_rank = int(cnt+1-43-ad_cnt/2) # ad_cnt 광고수/ 
                    print(new_pg,'페이지 내에서',one_page_rank,'순위')

                    # 네이버쇼핑 url
                    naver_shopping_url = f'https://search.shopping.naver.com/search/all?origQuery={find_word_1}&pagingIndex={new_pg}&pagingSize=40&productSet=total&query={find_word_1}&sort=rel&timestamp=&viewType=list'
                    stop_log = True
                    print('네이버쇼핑 url:',naver_shopping_url)
                    correct_word_list.append([{'상품명':f'{productTitle}','전체 상품 순위':f'{all_rank}','페이지':f'{new_pg}','순위':f'{one_page_rank}','url':{naver_shopping_url}}])
                    # print('상품 상세페이지 url:',pdturl)
                    # break
            
        if stop_log == True:
            break
        else:
            print('찾는 상품이 없습니다.')






        


