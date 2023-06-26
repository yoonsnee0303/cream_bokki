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


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("no-sandbox")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("prefs", {"prfile.managed_default_content_setting.images": 2})
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
#options.add_argument('headless')            # headless모드 (창 비활성화)
options.add_argument('disable-gpu')         # GPU 가속 종료
options.add_argument("lang=ko_KR")          # 가짜 플러그인 탑재


# HTML 파일 읽기
with open('html_files.txt', 'r', encoding='utf-8') as file:
    html_text = file.read()

# BeautifulSoup 객체 생성
soup = bs(html_text, 'html.parser')

li_tags = soup.find_all('li', {'class': 'scp-component-category-item'})

label_tags = soup.find_all('label')
cnt = 0
tag_list = []
for tag in label_tags:
    if str(tag).__contains__('for="component'):
        parent = tag.parent
        if not str(parent).__contains__('href'):
            cnt += 1
            tag = str(tag).split(sep='=')[1].split(sep='t')[1].split(sep='"')[0]
            tag_list.append(tag)

tag_list = tag_list[1:]


# CSV 파일을 쓰기 모드로 열기
def process_urls(tag_list,list_start,list_end):
    print(list_start, list_end)
    # for num,tag in enumerate(tag_list,start=list_start):
    for i in range(list_start, list_end):
        print(i, '/', list_end)
        tag = tag_list[i]

        driver = webdriver.Chrome(options=options)
        url = f'https://store.coupang.com/vp/vendors/A00037308/product/lists?componentId={tag}&pageNum=1'
        driver.get(url)
        elem = driver.find_element(By.TAG_NAME, 'body').text

        find_word = '"itemTotalCount":'
        total_cnt = elem[elem.find(find_word) + len(find_word):]
        total_cnt = int(total_cnt[:total_cnt.find(",")])

        cnt = math.ceil(int(total_cnt)/30)

        #if total cnt = 0?


        detail_url = []
        file_path = 'detail_url_2.csv'
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
            print(url)
            print(len(detail_url))
            time.sleep(1)

        with open(file_path, "a", newline='',encoding="utf-8") as f:
            writer = csv.writer(f)
            for url in detail_url:
                writer.writerow([url])
        time.sleep(2)
        # print(f'{num}/{len(tag_list)}')
        driver.close()

        # print(total_cnt)

        # cnt = math.ceil(int(total_cnt)/30)



import threading
total = len(tag_list)
num_intervals = 1 # thread 개수
interval_size = total // num_intervals

for i in range(num_intervals):
    start = i * interval_size + 1
    end = (i + 1) * interval_size


    if i == num_intervals - 1:
        end += total % num_intervals

    threads = []
    num_threads = num_intervals
    # print(start,'/',end)
    # print(num_threads)
    thread = threading.Thread(target=process_urls, args=(tag_list, start ,end))
    thread.start()
    threads.append(thread)