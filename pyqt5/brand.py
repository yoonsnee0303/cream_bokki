import requests
from bs4 import BeautifulSoup as bs
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

import time
import json
import os
import urllib3
import getpass
path_input = getpass.getuser()

import chromedriver_autoinstaller
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'C:/Users/{path_input}/AppData/Local/Programs/Python/Python310\{chrome_ver}/chromedriver.exe'
if os.path.exists(driver_path):
    print(f"chrome driver is installed: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
    chromedriver_autoinstaller.install(True)


brand_lists = ['11', 'lotte', 'sin', 'naver', 'today','gmarket', 'auction', 'interpark', 'coupang']
# brand_lists = ['today'] # test test test test test test 
brand_lists = ['coupang']

for brand in brand_lists:
    if brand == '11':
        json_data = []
        ll_lists = []
        for pg in range(1,9): #41
            url = f'https://search.11st.co.kr/Search.tmall?method=getSearchFilterAjax&kwd=동서가구+장인가구&pageNo={pg}&pageSize=250'
            response = requests.get(url)
            response_json = response.json()  # JSON 형식으로 변환
            for i in range(len(response_json['commonPrdList']['items'])):
                u = response_json['commonPrdList']['items'][i]['productDetailUrl']
                ll_lists.append(u)
                print(f"11번가 {len(ll_lists)}")
                print(u)
        # print(ll_lists)
        # print(len(set(ll_lists)))

        with open('11_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
            write = csv.writer(f)
            write.writerows([ll_lists])
        print(f'11번가 {len(ll_lists)} 상세페이지 파일 업로드')

    elif brand == 'lotte':
        url = 'https://www.lotteimall.com/search/searchMain.lotte?isTemplate=Y&headerQuery=장인가구&colldisplay=3200'
        response = requests.get(url)
        json_data = response.json()
        temp = json_data['body'][16]['data'] # 15
        # print(len(temp))
        lotte_lists = []
        for i in range(len(temp)):
            url = 'https://www.lotteimall.com/goods/viewGoodsDetail.lotte?goods_no=' + str(temp[i]['wishListMap']['goods_no'])
            lotte_lists.append(url)
            print(f'lotte {len(lotte_lists)}')
            print(url)
        with open('lot_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
            write = csv.writer(f)
            write.writerows([lotte_lists])
        print(f'롯데몰 {len(lotte_lists)} 상세페이지 파일 업로드')


    elif brand == 'sin':
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
        page = 1
        sin_lists = []
        while True:
            url = f'https://www.ssg.com/search.ssg?target=all&query=%EC%9E%A5%EC%9D%B8%EA%B0%80%EA%B5%AC%2B%EB%8F%99%EC%84%9C%EA%B0%80%EA%B5%AC&brand=2000020584&count=100&page={page}'
            res = requests.get(url, headers=headers, verify=False)

            ck_end = res.text.count('검색어와 일치하는 상품이 없습니다.')
            if ck_end == 1:
                #list_test csv파일로 저장
                with open('sin_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                    write = csv.writer(f)
                    write.writerows([sin_lists])
                break
            else:
                soup = bs(res.text, 'html.parser')
                elem = soup.find("ul", id="idProductImg")
                elems = elem.find_all("li")
                # print(len(elems))
                for el in elems:
                    url = el['id'].replace('item_unit_','https://www.ssg.com/item/itemView.ssg?itemId=')
                    sin_lists.append(url)
                    print(f'sin {len(sin_lists)}')
                    print(url)
                page += 1
                time.sleep(3)
        print(f'신세계 {len(sin_lists)} 상세페이지 파일 업로드')

    elif brand == 'naver':
        nav_lists = []
        find_word = '/newdf2013/products/'
        for page in range(1, 23):
            url = f'https://smartstore.naver.com/newdf2013/category/e78c2895503c4c4e993a71348c4cd9e8?st=POPULAR&dt=IMAGE&page={page}&size=40'
            res = requests.get(url)
            print(res.url)

            html = res.text
            cnt = html.count(find_word)

            for i in range(cnt):
                html = html[html.find(find_word)+len(find_word):]
                ea_url = 'https://smartstore.naver.com/newdf2013/products/' + html[:html.find('"')]
                nav_lists.append(ea_url)
                print(f'naver {len(nav_lists)}')
                print(ea_url)

            #list_test csv파일로 저장
            with open('nav_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                write = csv.writer(f)
                write.writerows([nav_lists])
        print(f'스마트스토어 {len(nav_lists)} 상세페이지 파일 업로드')

    elif brand == 'today':
        #옵션 - 셀레니움
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink_features=AutomationControlled")
        options.add_experimental_option("excludeSwitches",["enable_logging"])
        options.add_argument("no_sandbox")
        options.add_argument("--start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extionsions")
        options.add_experimental_option("useAutomationExtension",False)
        #options.add_argument("headless")
        options.add_argument("disable-gpu")
        options.add_argument("lang=ko_KR")
        driver = webdriver.Chrome(options=options)
        actions = ActionChains(driver)
        url = 'https://ohou.se/brands/home?query=%EC%9E%A5%EC%9D%B8%EA%B0%80%EA%B5%AC'

        driver.get(url)
        time.sleep(3)

        # Get the height of the viewport
        viewport_height = driver.execute_script("return window.innerHeight")

        # Define the amount to scroll
        scroll_height = 10000

        # Scroll down repeatedly
        o_lists = []
        while True:

            html = driver.page_source
            soup = bs(html, 'html.parser')

            #
            elems = soup.find_all('a', 'production-item__overlay')
            for el in elems:
                temp = 'https://ohou.se' + el['href']
                o_lists.append(temp)
                print(f'오늘의집 {len(o_lists)}')
                print(temp)
            o_lists = list(dict.fromkeys(o_lists))

            # Scroll down by the defined amount
            driver.execute_script(f"window.scrollBy(0, {scroll_height});")
            time.sleep(5)

            # get the current scroll position
            scroll_position = driver.execute_script("return window.pageYOffset;")


            #마지막 페이지 확인
            if 'temp_scroll_postion' in locals() and temp_scroll_postion == scroll_position:
                print('last page')
                # print(o_lists)
                print(len(o_lists))

                #list_test csv파일로 저장
                with open('o_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                    write = csv.writer(f)
                    write.writerows([o_lists])
                break


            #아니면 계속 리스트 수집
            temp_scroll_postion = scroll_position
                

        #아니면 계속 리스트 수집
        temp_scroll_postion = scroll_position
        print(f'오늘의집 {len(o_lists)} 상세페이지 파일 업로드')

    elif brand == 'gmarket':
        url = 'https://browse.gmarket.co.kr/search?keyword=장인가구+동서가구'
        response = requests.get(url)

        html_content = response.text
        soup = bs(html_content, 'html.parser')
        a_tags = soup.find_all('a', 'link__shop')

        url2 = 'http://item.gmarket.co.kr/Item?goodscode='
        gm_lists = []
        for tag in a_tags:
            tag = str(tag).split(' ')
            for t in tag:
                if 'data-montelena-goodscode' in t:
                    t = t.split('=')[1].replace('"','').replace("'","").replace("]","")
                    gm_lists.append(url2 + t)
                    print(f"지마켓 {len(gm_lists)})")
                    print(url2 + t)
        with open('gm_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
            write = csv.writer(f)
            write.writerows([gm_lists])  
        print(f'지마켓 {len(gm_lists)} 상세페이지 파일 업로드')
        
    elif brand == 'auction':
        auc_lists = []
        for pg in range(1,6):
            url = f'https://browse.auction.co.kr/search?keyword=%ec%9e%a5%ec%9d%b8%ea%b0%80%ea%b5%ac%2b%eb%8f%99%ec%84%9c%ea%b0%80%ea%b5%ac&itemno=&nickname=&encKeyword=%25EC%259E%25A5%25EC%259D%25B8%25EA%25B0%2580%25EA%25B5%25AC%252B%25EB%258F%2599%25EC%2584%259C%25EA%25B0%2580%25EA%25B5%25AC&arraycategory=&frm=&dom=auction&isSuggestion=No&retry=&k=0&p={pg}'
            response = requests.get(url)

            html_content = response.text
            soup = bs(html_content, 'html.parser')
            a_tags = soup.find_all('a')

            hrefs = [a_tag['href'] for a_tag in a_tags if 'href' in a_tag.attrs if 'itempage3' in a_tag['href']]
            hrefs = hrefs[::2]
            for href in hrefs:
                auc_lists.append(href)
                print(f'옥션 {len(auc_lists)}')
                print(href)
            # print(url)
            # print(pg,'/5')

        with open('auc_list.csv', "w", newline='',encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerows([auc_lists])
        print(f'옥션 {len(auc_lists)} 상세페이지 파일 업로드')

    elif brand == 'interpark':
        url_data = []
        for i in range(134):
            try:
                url = f'https://shopping.interpark.com/niSearch/shop/listPrdChoiceAndNormal.json?pis1=shop&page={i+1}&keyword=장인가구&rows=52'
                res = requests.get(url)
                data = json.loads(res.text)
                cnt = len(data['data']['listChoiceAndNormal'][0])
                for j in range(cnt+1):
                    try:
                        item_url = 'https://shopping.interpark.com/product/productInfo.do?prdNo=' + str(data['data']['listChoiceAndNormal'][j]['prdNo'])
                        # print(f'{j}/{item_url}')
                        # print(cnt)
                        url_data.append(item_url)
                        print(f'인터파크 {len(url_data)}')
                        print(item_url)
                    except:
                        pass
            except:
                pass
        
        #list_test csv파일로 저장
        with open('inter_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
            write = csv.writer(f)
            write.writerows([url_data])
        print(f'인터파크 {len(url_data)} 상세페이지 파일 업로드')
        
    elif brand == 'coupang':
        #옵션 - 셀레니움
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink_features=AutomationControlled")
        options.add_experimental_option("excludeSwitches",["enable_logging"])
        options.add_argument("no_sandbox")
        options.add_argument("--start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extionsions")
        options.add_experimental_option("useAutomationExtension",False)
        #options.add_argument("headless")
        options.add_argument("disable-gpu")
        options.add_argument("lang=ko_KR")
        driver = webdriver.Chrome(options=options)
        actions = ActionChains(driver)

        # 웹페이지 접속
        driver.get("https://store.coupang.com/vp/vendors/A00037308/products")

        # 전체 페이지 높이를 저장합니다.
        page_height = driver.execute_script("return document.body.scrollHeight")

        # y축을 전체 높이의 1/3까지 내립니다.
        scroll_height = page_height // 2.5
        driver.execute_script("window.scrollTo(0, {});".format(scroll_height))


        ul_elements = driver.find_elements(By.CLASS_NAME, 'scp-component-filter-options__option-items__btn-fold')
        time.sleep(2)
        for ul_element in ul_elements:
            driver.execute_script("arguments[0].click();", ul_element)
            time.sleep(1.5)
        html = driver.page_source
        with open('html_files.txt', 'w',encoding='utf-8') as f:
            f.write(html)

        soup = bs(html,'html.parser')
        li_tags = soup.find_all('li', {'class': 'scp-component-category-item'})


        label_tags = soup.find_all('label')
        cnt = 0
        tag_list = []
        for tag in label_tags:
            if str(tag).__contains__('for="component'):
                parent = tag.parent
                if not str(parent).__contains__ ('href'):
                    cnt+=1
                    tag = str(tag).split(sep='=')[1].split(sep='t')[1].split(sep='"')[0]
                    tag_list.append(tag)
            

        tag_list = tag_list[1:]

        url_list = []
        for tag in tag_list:
            url = f'https://store.coupang.com/vp/vendors/A00037308/product/lists?componentId={tag}&pageNum=1'
            url_list.append(url)
        print(len(url_list))
        print(tag_list)

        # CSV 파일을 쓰기 모드로 열기

        for num,tag in enumerate(tag_list,start=1):

                driver = webdriver.Chrome(options=options)
                actions = ActionChains(driver)

                # # driver.get(url)
                url = f'https://store.coupang.com/vp/vendors/A00037308/product/lists?componentId={tag}&pageNum=1'
                driver.get(url)
                elem = driver.find_element(By.TAG_NAME, 'body').text

                find_word = '"itemTotalCount":'
                total_cnt = elem[elem.find(find_word) + len(find_word):]
                total_cnt = total_cnt[:total_cnt.find(",")]
                print(total_cnt)

                detail_url = []
                file_path = 'detail_url.csv'
                for pageNum in range(1, cnt+1): 
                    url = f'https://store.coupang.com/vp/vendors/A00037308/product/lists?componentId={tag}&pageNum={str(pageNum)}'
                    driver.get(url)
                    find_word = 'link'
                    elem = driver.find_element(By.TAG_NAME, 'body').text
                    cnt = elem.count(find_word)
                    for i in range(cnt):
                        search2 = elem[elem.find(find_word) + len(find_word)+3:]
                        elem = search2
                        search2 = search2[:search2.find('"')]
                        detail_url.append(search2)
                with open(file_path, "a", newline='',encoding="utf-8") as f:
                    writer = csv.writer(f)
                    for url in detail_url:
                        writer.writerow([url])
                time.sleep(2)
                print(f'{num}/{len(tag_list)}')
                driver.close()                
