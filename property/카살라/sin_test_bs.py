from bs4 import BeautifulSoup as bs
import csv
import selenium

import urllib3
import os

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
from selenium.webdriver.common.alert import Alert


import chromedriver_autoinstaller
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'C:/Users/{path_input}/AppData/Local/Programs/Python/Python310\{chrome_ver}/chromedriver.exe'
if os.path.exists(driver_path):
    print(f"chrome driver is installed: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
    chromedriver_autoinstaller.install(True)

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink_features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable_logging"])
options.add_argument("no_sandbox")
options.add_argument("--start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extionsions")
options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("headless")
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")
# driver = webdriver.Chrome(options=options)
# actions = ActionChains(driver)


# for pg in range(1,25):
#     url = f'https://www.ssg.com/search.ssg?target=all&query=동서카살라&count=100&page={pg}'
#     print(f'{pg}/25페이지')

#     driver.get(url)

import requests
import time


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
page = 1


url_list = []
for pg in range(1,25): #22,23
    url = f'https://www.ssg.com/search.ssg?target=all&query=동서카살라&count=100&page={pg}' # 100개씩 보기, 현재 페이지: page 1~24페이지까지 수집 예정
    print(f'{pg}/25페이지')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': 'Bearer your-access-token'
    }

    req = requests.get(url,verify=False,headers=headers) # 신세계는 반드시 헤드값 넣어주어야함.
    html = req.text
    soup = bs(html,'html.parser')
    names = soup.find_all(class_='cunit_prod') # 상품 각 클래스
    if names == None:
        print(pg)
    print(type(names))
    for name in names:
        a_tags = name.find_all('a', attrs={'data-info': True})
        for a_tag in a_tags:
            url_list.append(a_tag)
            print(a_tag)
        print('현재 수집된 상세페이지: ', len(url_list))
    time.sleep(1)

print(len(url_list))
with open('sin_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
    write = csv.writer(f)
    write.writerows([url_list])
