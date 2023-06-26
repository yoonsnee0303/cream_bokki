from bs4 import BeautifulSoup as bs
import csv
import os
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
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







import time

def get_tag(driver):
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
    # actions = ActionChains(driver)
    # 웹페이지 접속
    driver.get("https://store.coupang.com/vp/vendors/A00037308/products")

    driver.find_element(By.CLASS_NAME,'scp-component-filter-options__fold-items').click() # 더보기


    # 전체 페이지 높이를 저장합니다.
    page_height = driver.execute_script("return document.body.scrollHeight")

    # y축을 전체 높이의 1/3까지 내립니다.
    scroll_height = page_height // 2.5
    driver.execute_script("window.scrollTo(0, {});".format(scroll_height))


    ul_elements = driver.find_elements(By.CLASS_NAME,'scp-component-filter-options__option-items__btn-fold')
    for ul_element in ul_elements:
        driver.execute_script("arguments[0].click();", ul_element) # 버튼 클릭
        time.sleep(0.03)
    html = driver.page_source
    # 파일 쓰기 모드로 열기
    # with open('html_files.txt', 'w',encoding='utf-8') as f:
    #     # 파일에 쓸 내용 작성
    #     f.write(html)
    soup = bs(html,'html.parser')

    # 상품번호
    label_tags = soup.find_all('label')
    cnt = 0
    tag_list = []
    for tag in label_tags:
        if str(tag).__contains__('for="component'):
            parent = tag.parent

            if not str(parent).__contains__ ('href'):
                cnt+=1
                tag = str(tag).split(sep='=')[1].split(sep='t')[1].split(sep='"')[0]
                print(tag)
                tag_list.append(tag)
    tag_list = tag_list[1:]
    print(tag_list)
    print(len(tag_list))

    # url_list = []
    # for tag in tag_list:
    #     url = f'https://store.coupang.com/vp/vendors/A00037308/product/lists?componentId={tag}&pageNum=1'
    #     url_list.append(url)
    # print(len(url_list))
    return tag_list




def process_urls(tag_list,list_start,list_end):


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
    # for num,tag in enumerate(tag_list,start=list_start):
    for i in range(list_start, list_end):
        print(i, '/', list_end)
        tag = tag_list[i]

        url = f'https://store.coupang.com/vp/vendors/A00037308/product/lists?componentId={tag}&pageNum=1'
        driver.get(url)
        elem = driver.find_element(By.TAG_NAME, 'body').text
        find_word = '"itemTotalCount":'
        try:
            total_cnt = elem[elem.find(find_word) + len(find_word):]
            total_cnt = int(total_cnt[:total_cnt.find(",")])
            cnt = math.ceil(int(total_cnt)/30)

            file_path = 'cou_lists.csv'
            detail_url = []
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
            # driver.close()
        except:
            pass


def thread_function(tag_list, start, end):
    # process_urls 함수를 실행하고 결과를 받아옴
    result = process_urls(tag_list, start, end)
    
    # 결과를 받아왔으므로 Lock을 얻어 결과를 추가
    with result_lock:
        results.append(result)
        
        # 모든 결과를 받아왔을 때, notify를 호출하여 대기 중인 스레드를 깨움
        if len(results) == num_intervals:
            result_available.notify_all()




import threading

# Lock 객체 생성
result_lock = threading.Lock()

# Condition 객체 생성
result_available = threading.Condition(lock=result_lock)

# 공유 변수
results = []

threads = []
tag_list = get_tag(webdriver)
total = len(tag_list)
num_intervals = 2 # thread 개수
interval_size = total // num_intervals

for i in range(num_intervals):
    start = i * interval_size + 1
    end = (i + 1) * interval_size

    if i == num_intervals - 1:
        end += total % num_intervals

    # 스레드 생성
    thread = threading.Thread(target=thread_function, args=(tag_list, start, end))
    thread.start()
    threads.append(thread)

# # 모든 스레드가 결과를 받아올 때까지 대기
# with result_available:
#     while len(results) < num_intervals:
#         result_available.wait()





# # 모든 스레드의 실행이 완료될 때까지 대기
# for thread in threads:
#     thread.join()
