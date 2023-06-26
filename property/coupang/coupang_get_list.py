from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import csv
import math
import threading
import time
import os
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



see_more = driver.find_element(By.CLASS_NAME, 'scp-component-filter-options__fold-items').click()
ul_elements = driver.find_elements(By.CLASS_NAME,'scp-component-filter-options__option-items__btn-fold')
for ul_element in ul_elements:
    driver.execute_script("arguments[0].click();", ul_element) # 버튼 클릭
    print(ul_element.text)
    time.sleep(.1)
html = driver.page_source
soup = bs(html,'html.parser')
# 파일 쓰기 모드로 열기
# with open('cou_html_files.txt', 'w',encoding='utf-8') as f:
#     # 파일에 쓸 내용 작성
#     f.write(html)

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
        file_path = 'cou_list.csv'
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
        time.sleep(5)
        # print(f'{num}/{len(tag_list)}')
        driver.close()

        # print(total_cnt)

        # cnt = math.ceil(int(total_cnt)/30)



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












