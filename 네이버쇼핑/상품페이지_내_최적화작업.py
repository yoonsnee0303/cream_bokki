import os
import time
import random
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
driver_path = f'C:/Users/{path_input}/AppData/Local/Programs/Python/Python310\{chrome_ver}/chromedriver.exe'
if os.path.exists(driver_path):
    print(f"chrome driver is installed: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
    chromedriver_autoinstaller.install(True)

# 옵션 - 셀레니움
options = webdriver.ChromeOptions()
options.add_argument(
    "--disable-blink_features=AutomationControlled")
options.add_experimental_option(
    "excludeSwitches", ["enable_logging"])
options.add_argument("no_sandbox")
options.add_argument("--start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extionsions")
options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("headless")
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")
driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)


driver.get("https://smartstore.naver.com/dongsuhfurniture/products/4852764378")
time.sleep(2)

from 스크롤 import 스크롤
from 스크롤 import 스크롤_탑

def 옵션_클릭(driver):
    print('옵션_클릭')
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

def 톡톡문의_찜하기_장바구니_클릭(driver):

    dicts = {
                0:'톡톡문의',
                1:'찜하기',
                2:'장바구니',
            }

    num = random.randint(0,len(dicts)-1)
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

    try:
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except:
        pass

    time.sleep((random.randint(1000,4000)/1000))
    스크롤_탑(driver)

def 포토_동영상_리뷰_보기(driver):

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

def 베스트_상품_보기(driver):

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

def 상세정보_리뷰_QA_반품교환정보_보기(driver):

    dicts = {
                0:'상세정보',
            }

    num = random.randint(0,0)
    스크롤(driver, 40, 100, dicts[num], 0)
    time.sleep(2)

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

    if set(all_round) == {'0', '1', '2', '3'}:

        #옵션 선택
        dicts[4](driver)

        #쿠키 제거
        driver.delete_all_cookies()

        #종료
        driver.quit()
        print('[끄-으-읕]')
        break