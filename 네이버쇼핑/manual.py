from 스크롤 import *
from datetime import datetime
from fake_useragent import UserAgent
import random
import requests
import pyautogui
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


import os
import urllib3
import getpass
path_input = getpass.getuser()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert


import chromedriver_autoinstaller
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'C://Users//{path_input}//AppData//Local//Programs//Python//Python310//{chrome_ver}//chromedriver.exe'
if os.path.exists(driver_path):
    print(f"chrome driver is installed: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
chromedriver_autoinstaller.install(True)



import sh_word
import numpy as np

def sleep_random():
    time.sleep(random.randint(1000, 2500)/1000)

# 셀레니움 세팅
# create a UserAgent object
# ua = UserAgent()
# user_agents = []
# for i in range(1,10):
#     user_agent = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{i}{i}{i}.0.0.0 Safari/537.36'
#     user_agents.append(user_agent)
# user_agents = np.random.choice(user_agents)

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0.2',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 Edg/92.0.902.55',
]

# referers = [
#     'https://www.google.com/',
#     'https://www.bing.com/',
#     'https://www.yahoo.com/',
#     'https://www.duckduckgo.com/',
# ]




def selenium_setting(url):
    print('selenium_setting_S')
    # create Chrome options with random user agent and headers
    options = webdriver.ChromeOptions()
    user_agent = random.choice(user_agents)
    options.add_argument(f'user-agent={user_agent}')
    # options.add_argument(f'referer={random.choice(referers)}')
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    print('설정된 헤더 값: ',user_agent)
    # navigate to the URL
    driver.get(url)
    user_agent = driver.execute_script("return navigator.userAgent;")
    # referer = driver.execute_script("return document.referrer;")
    # save the header log
    with open('2023-04-05 로그기록', 'a',newline='',encoding='utf_8_sig') as f:
        f.write('{} 설정된 헤더 값: {} /실제 받아온 헤더: {}\n'.format(datetime.now(), user_agents, user_agent))
    # get the page source
    page_source = driver.page_source
    return driver, page_source
print('selenium_setting_E')

# def search_zum_for_naver(driver):
#     print('search_zum_for_naver_S')
#     # navigate to Google and search for "zum"
#     search_box = driver.find_element(By.NAME,'q')
#     search_box.send_keys('zum')
#     time.sleep(2)
#     search_box.send_keys(Keys.RETURN)

#     # click the first search result for Zum
#     time.sleep(2)
#     zum_link = driver.find_element(By.LINK_TEXT,'ZUM - 세상을 읽다, ZUM')
#     zum_link.click()

#     # find the search box element and enter "naver"
#     time.sleep(2)
#     search_box = driver.find_element(By.NAME,'query')
#     search_box.send_keys('naver')

#     # click the search button
#     time.sleep(2)
#     search_button = driver.find_element(By.LINK_TEXT,'네이버')
#     search_button.click()
#     time.sleep(2)
#     print('search_zum_for_naver_E')


num=5

# 사전_단어_검색_뻘짓()
def search_word_in_url(driver):
    
    # read the file to obtain the search query
    print('사전_단어_검색_뻘짓_S')
    num_searches = random.randint(5,9)
    # num_searches = 3
    for i in range(2,num_searches):
        wd = sh_word.sh_word.split('\n')
        wd.pop()
        words = random.choice([i for i in wd])
        separte_word = [i for i in words]

        wait_time = random.randint(1, 3) 
        print(f"Waiting for {wait_time} seconds before searching again...")
        time.sleep(wait_time)

        # find the search bar element and enter the search query
        search_bar = driver.find_element(By.NAME,"query") # 네이버 검색창

        for 워드 in range(len(separte_word)):
            search_bar.send_keys(separte_word[워드])
            time.sleep(random.randint(1000, 2500)/1000)
        search_bar.send_keys(Keys.RETURN) # 엔터
        time.sleep(random.randint(1000, 2500)/1000)
        driver.find_element(By.NAME,"query").clear()
        print(f"Search {i+1} of {num_searches} completed.")

    # search_bar.send_keys(separte_word[워드])
    
        
    print('사전_단어_검색_뻘짓_E')
    


    
# 사전_단어 검색했을 시 카테고리 클릭
def category_click(driver):
    print('category_click_S')
    #통합, 어학사전, VIEW, 이미지, 지식iN, 쇼핑, 뉴스, 지도
    category = random.choice(['통합', 'VIEW', '이미지', '지식iN', '뉴스'])
    print(f'press the {category}')
    driver.find_element(By.LINK_TEXT,category).click()
    simple_스크롤(driver,2)
    time.sleep(random.randint(1000, 2500)/1000)
    print('category_click_E')



# 네이버 쇼핑 들어가는 경로 - 1: 쇼핑 버튼 누르기, 0: 네이버에서 '쇼핑' 검색
def enter_navershopping(driver):   
    print('enter_navershopping_S')
    ran = random.randint(0,1)
    driver.find_element(By.CLASS_NAME,'link').click() # 초기화면
    time.sleep(random.randint(2500, 3000)/1000)

    if ran == 1:
        print('enter_navershopping: 초기화면에서 쇼핑 버튼 찾아 들어가기')
        category_word = '쇼핑'
        driver.find_element(By.LINK_TEXT,category_word).click()

    else:
        print('enter_navershopping: 초기화면에서 네이버 쇼핑 검색하여 들어가기')
        search_bar= driver.find_element(By.NAME,'query')
        search_bar.send_keys('네이버 쇼핑')
        time.sleep(random.randint(1000, 2500)/1000)

        search_bar.send_keys(Keys.RETURN)
        time.sleep(random.randint(1000, 2500)/1000)

        driver.find_element(By.PARTIAL_LINK_TEXT,'네이버쇼핑').click()
        time.sleep(random.randint(1000, 2500)/1000)
    

    

# # 사전_단어_검색_뻘짓2()
# def search_word_in_url2(driver):
#     # read the file to obtain the search query
#     print('사전_단어_검색_뻘짓2_S')
#     driver.find_element(By.CLASS_NAME,"_searchInput_search_text_3CUDs").click()
#     num_searches = random.randint(4,8)

#     for i in range(2,num_searches):
#         wd = sh_word.sh_word.split('\n')
#         wd.pop()
#         words = random.choice([i for i in wd])
#         separte_word = [i for i in words]

#         wait_time = random.randint(1, 3) 
#         print(f"사전_단어_검색_뻘짓2_S: Waiting for {wait_time} seconds before searching again...")
#         time.sleep(wait_time)

#         # find the search bar element and enter the search query
#         search_bar = driver.find_element(By.CLASS_NAME,"_searchInput_search_text_3CUDs") # 네이버 검색창

#         for 워드 in range(len(separte_word)):
#             search_bar.send_keys(separte_word[워드])
#             time.sleep(random.randint(1000, 2500)/1000)
#         search_bar.send_keys(Keys.RETURN) # 엔터
#         time.sleep(random.randint(1000, 2500)/1000)
#         driver.find_element(By.CLASS_NAME,"_searchInput_search_text_3CUDs").clear()
#         time.sleep(2)
#         driver.back() # 뒤로가기
#         print(f"Search {i+1} of {num_searches} completed.")
#     print('사전_단어_검색_뻘짓2_E')

# 메인 키워드 검색하고, 원부페이지 들어가기
def search_ds(driver):
    try:
        print('search_ds_S')
        driver.switch_to.window(driver.window_handles[-1])
        search_bar = driver.find_element(By.CLASS_NAME,'_searchInput_search_text_3CUDs')
        search_bar.send_keys(random.choice(['나이키','딸기', '키보드', '물통', '바디크림', '모니터', '물티슈', '휴지', '우산', 'e']))
        search_bar.send_keys(Keys.RETURN) # 엔터
        time.sleep(random.randint(1000, 2500)/1000)
        driver.back()
        time.sleep(random.randint(1000, 2500)/1000)
        search_bar = driver.find_element(By.CLASS_NAME,'_searchInput_search_text_3CUDs')
        search_word = random.choice(['동서가구 소파','동서가구 쇼파', '동서가구소파','동서가구쇼파'])
        time.sleep(random.randint(1000, 2500)/1000)
        search_bar.click()
        time.sleep(random.randint(1000, 2500)/1000)
        search_bar.send_keys(search_word) # 입력
        time.sleep(random.randint(1000, 2500)/1000)
        search_bar.send_keys(Keys.RETURN) # 엔터

        time.sleep(random.randint(1000,2000)/1000)
        html = driver.page_source
        if html.count("검색어가 입력되지 않았습니다.") > 0:
            print("검색어가 입력되지 않았습니다.")
            return 'error'
        print('enter_navershopping_E')


        스크롤(driver, 40, 100,'헤드레스트',1)
        time.sleep(random.randint(1000, 2500)/1000)
        driver.find_element(By.PARTIAL_LINK_TEXT,'헤드레스트').click()
        time.sleep(random.randint(1000, 2500)/1000)
        driver.switch_to.window(driver.window_handles[-1])
        # 스크롤(driver,0,0,'사업자등록번호 : 220-81-62517',0)ㅊ
        time.sleep(4)
        
        # Find the tbody element using its tag name
        ran = random.randint(0,1)
        if ran == 0:
            print('search_ds: 원부페이지 동서가구 접속_스크롤 없음')
            driver.find_element(By.CLASS_NAME,'productByMall_mall__SIa50').click() 
            time.sleep(random.randint(1000, 2500)/1000)
        else:
            print('search_ds: 원부페이지 동서가구 접속_스크롤 있음')
            스크롤(driver,40,100,'최저가순',0)
            time.sleep(random.randint(1000, 2500)/1000)
            driver.find_element(By.CLASS_NAME,'productList_title__R1qZP').click()
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(random.randint(1000, 2500)/1000)
    except:
        스크롤_탑(driver)
    print('search_ds_E')
    


# 옵션

def 옵션_클릭(driver):
    print('옵션_클릭_S')
    스크롤(driver, 40, 100, '', 5)

    #1번옵션 랜덤선택
    elem = driver.find_element(By.CLASS_NAME, 'bd_2dy3Y')
    elems = elem.find_elements(By.TAG_NAME, 'a')
    elems[0].click()
    time.sleep((random.randint(1000,4000)/1000))
    elems2 = driver.find_elements(By.CLASS_NAME, 'bd_1y1pd')
    num = random.randint(0, len(elems2)-1)
    elems2[num].click()

    #2번옵션 랜덤선택
    elem = driver.find_element(By.CLASS_NAME, 'bd_2dy3Y')
    elems = elem.find_elements(By.TAG_NAME, 'a')
    elems[1].click()
    time.sleep((random.randint(1000,4000)/1000))
    elems2 = driver.find_elements(By.CLASS_NAME, 'bd_1y1pd')
    num = random.randint(0, len(elems2)-1)
    elems2[num].click()

    time.sleep((random.randint(1000,4000)/1000))
    print('옵션_클릭_E')


def 톡톡문의_찜하기_장바구니_클릭(driver):
    print('톡톡문의_찜하기_장바구니_클릭_S')

    dicts = {
                0:'톡톡문의',
                1:'찜하기',
                2:'장바구니',
                3:'구매하기'
            }

    num = random.randint(0,len(dicts))
    num = 0
    스크롤(driver, 40, 100, dicts[num], 0)
    elem = driver.find_element(By.LINK_TEXT, dicts[num])
    print(dicts[num])
    elem.click()

    time.sleep((random.randint(1000,4000)/1000))
    try:
        alert = Alert(driver)
        alert.dismiss()
        print('alert close')
    except:
        pass
    # if num==0:
    #     driver.switch_to.window(driver.window_handles[-1]) # 팝업창을 선택
    #     driver.close()
    #     driver.switch_to.window(driver.window_handles[2]) # 팝업창을 선택
    #     time.sleep(2)
    # else:
    #     try:
    #         alert = Alert(driver)
    #         alert.dismiss()
    #         print('alert close')
    #     except:
    #         pass


    time.sleep((random.randint(1000,4000)/1000))
    스크롤_탑(driver)
    print('톡톡문의_찜하기_장바구니_클릭_E')


def 포토_동영상_리뷰_보기(driver):
    print('포토_동영상_리뷰_보기_S')

    try:
        dicts = {
                    0:'포토/동영상',
                }

        스크롤(driver, 40, 100, dicts[0], 0)
        elem = driver.find_element(By.LINK_TEXT, dicts[0])
        time.sleep((random.randint(1000,4000)/1000))

        elem = driver.find_element(By.CLASS_NAME, '_2FGBFs3BuT')
        elems = elem.find_elements(By.TAG_NAME, 'a')

        num = random.randint(2,5)
        print(f'포토_동영상_리뷰_보기({num})')

        for i in range(num):
            elems[1].click()
            gap = random.randint(3000,8000)
            print(gap)
            time.sleep(gap / 1000)

        time.sleep((random.randint(1000,4000)/1000))
        스크롤_탑(driver)
    except:
        스크롤_탑(driver)
    print('포토_동영상_리뷰_보기_E')

def 베스트_상품_보기(driver):
    print('베스트_상품_보기_S')
    try:
        dicts = {
                    0:'포토/동영상',
                }

        스크롤(driver, 40, 100, dicts[0], 0)
        elem = driver.find_element(By.LINK_TEXT, dicts[0])
        time.sleep((random.randint(1000,4000)/1000))

        elem = driver.find_element(By.CLASS_NAME, '_1IPlkE4XNY')
        elems = elem.find_elements(By.TAG_NAME, 'button')

        num = random.randint(4,8)
        print(f'베스트_상품_보기({num})')
        for i in range(num):
            elems[1].click()
            gap = random.randint(1000,4000)
            print(gap)
            time.sleep(gap / 1000)

        time.sleep((random.randint(1000,4000)/1000))
        스크롤_탑(driver)
    except:
        스크롤_탑(driver)
    print('베스트_상품_보기_E')

def 상세정보_리뷰_QA_반품교환정보_보기(driver):
    print('상세정보_리뷰_QA_반품교환정보_보기_S')
    try:
        dicts = {
                    0:'상세정보',
                }

        num = random.randint(0,0)
        스크롤(driver, 40, 100, dicts[num], 0)
        time.sleep(random.randint(1000, 2500)/1000)

        elems = driver.find_elements(By.CLASS_NAME, '_1k5R-niA93')
        num = random.randint(0,3)
        elems[num].click()
        gap = random.randint(3000,8000)
        print(gap)
        time.sleep(gap / 1000)

        duration = random.randint(2,9)
        print(f'상세정보_리뷰_QA_반품교환정보_보기({duration})')
        스크롤(driver, 40, 100, '', duration)

        스크롤_탑(driver)
    except:
        스크롤_탑(driver)
    print('상세정보_리뷰_QA_반품교환정보_보기_E')

import numpy as np
# example usage
while True:
    for i in range(1,20000):
        from 스크롤 import *
        from fake_useragent import UserAgent
        import random
        import requests
        import pyautogui
        import time

        from selenium import webdriver
        from selenium.webdriver.common.by import By


        import os
        import urllib3
        import getpass
        path_input = getpass.getuser()

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.support.select import Select
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.common.alert import Alert


        import chromedriver_autoinstaller
        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
        driver_path = f'C://Users//{path_input}//AppData//Local//Programs//Python//Python310//{chrome_ver}//chromedriver.exe'
        if os.path.exists(driver_path):
            print(f"chrome driver is installed: {driver_path}")
        else:
            print(f"install the chrome driver(ver: {chrome_ver})")
        chromedriver_autoinstaller.install(True)



        import sh_word
        import numpy as np



        
        url = 'https://www.google.com/search?q=%EB%84%A4%EC%9D%B4%EB%B2%84'
        driver, response = selenium_setting(url)

        time.sleep(1)
        search_box = driver.find_element(By.PARTIAL_LINK_TEXT, 'naver')
        search_box.click()

        time.sleep(random.randint(2000, 2500)/1000)
        search_word_in_url(driver)
        time.sleep(random.randint(4000, 4500)/1000)
        category_click(driver)
        time.sleep(random.randint(4000, 4500)/1000)
        er_ck = enter_navershopping(driver)
        if er_ck == 'error':
            driver.quit()
            print("에러발생 line:383 fun:  enter_navershopping")
            time.sleep(3)
            break
        time.sleep(random.randint(4000, 4500)/1000)
        er_ck = search_ds(driver)
        if er_ck == 'error':
            driver.quit()
            print("에러발생 line:496 fun:  enter_navershopping")
            time.sleep(3)
            break

        dicts = {
            0 : 톡톡문의_찜하기_장바구니_클릭,
            1 : 포토_동영상_리뷰_보기,
            2 : 베스트_상품_보기,
            3 : 상세정보_리뷰_QA_반품교환정보_보기,
            4 : 옵션_클릭
        }


        #main #main #main #main #main #main #main #main
        #main #main #main #main #main #main #main #main
        all_round = ''
        while True:
            num = random.randint(0, len(dicts)-2) 
            all_round += str(num)
            print(f'all_round: {all_round}')
            dicts[num](driver)  # call the function/method at dicts[num]

            # if set(all_round) == {'0', '1', '2', '3'}:
            if len(all_round) > 0:

                #옵션 선택
                dicts[4](driver)

                #쿠키 제거
                driver.delete_all_cookies()

                #종료
                driver.quit()

                time.sleep(5)
                print('[끄-으-읕]')
                break
        print(f'{i}번째 완료')




