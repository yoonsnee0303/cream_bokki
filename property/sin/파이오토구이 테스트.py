# 모든 텍스트를 긁어모아서 pyautogui로 캡처

import pyautogui
import getpass
path_input = getpass.getuser()
import urllib3
import os
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
actions = ActionChains(driver)


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
import chromedriver_autoinstaller

path_input = getpass.getuser()

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'C://Users//{path_input}//AppData//Local//Programs//Python//Python310//{chrome_ver}//chromedriver.exe'

if os.path.exists(driver_path):
    print(f"chrome driver is installed: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
chromedriver_autoinstaller.install(True)

url = 'https://www.ssg.com/item/itemView.ssg?itemId=1000031541823'
url_name = driver.current_url
print(url_name)


import datetime
now = datetime.datetime.now()

def pictures(url,location):
    driver.execute_script(f"window.scrollTo({location['x']},{location['y']})")
    driver.get_screenshot_as_png(['시간:{},신세계,상품명(url섞인거)'.format(now)])
    

def scroll_webpage(url,scroll_distance):
    driver.get(url)
    time.sleep(2)
    cdtl_row_top = driver.find_element(By.CLASS_NAME,"cdtl_row_top")
    cdtl_cont_info = driver.find_elements(By.CLASS_NAME,"cdtl_cont_info")
    locations = [page.location for page in cdtl_cont_info]
    for loc in locations:
        pictures(url,loc)
        time.sleep(3)
    time.sleep(1000)

    # loc for in range(len(cont_info_locations)):
    #     driver.execute_script(f"window.scrollTo({cont_info.locations[loc]['x']},{cdtl_cont_info.location['y']})")



    # 지정 좌표로 스크롤 이동
    driver.execute_script("window.scrollTo(0, 0)")
    
    # Get current height of the webpage
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
            # Scroll down the webpage
            driver.execute_script(f"window.scrollTo(0, {scroll_distance});")
            time.sleep(2)

            # Check if '동서' is found in any element
            cdtl_row_top = driver.find_element(By.CLASS_NAME,"cdtl_row_top")
            cdtl_cont_info = driver.find_element(By.CLASS_NAME,"cdtl_cont_info")
            print(cdtl_row_top.location)
            print(cdtl_cont_info.location)
            pyautogui.moveTo(0,2064)
            time.sleep(1000)
            for elem in cdtl_row_top + cdtl_cont_info:
                if '동서' in elem.text:
                    print("Found '동서' in element:", elem.tag_name)
                    
                    # driver.quit()
                    return True

            # Get the new height of the webpage
            new_height = driver.execute_script("return document.body.scrollHeight")

            # Check if we have reached the end of the webpage
            if new_height == last_height:
                break

            last_height = new_height

            driver.quit()

    return False

url = 'https://www.ssg.com/item/itemView.ssg?itemId=1000062154358&siteNo=6004&salestrNo=6005&tlidSrchWd=%EA%B0%80%EA%B5%AC&srchPgNo=1&src_area=ssglist'
scroll_webpage(url,200)

