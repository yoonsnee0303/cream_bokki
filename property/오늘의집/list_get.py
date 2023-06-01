import time
import csv
import getpass
path_input = getpass.getuser()



from matplotlib import pyplot as plt


from bs4 import BeautifulSoup as bs
import os
import urllib3
import csv


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

#오늘의집
url = 'https://ohou.se/brands/home?query=%EC%9E%A5%EC%9D%B8%EA%B0%80%EA%B5%AC'


driver.get(url)
time.sleep(3)

# Get the height of the viewport
viewport_height = driver.execute_script("return window.innerHeight")

# Define the amount to scroll
scroll_height = 10000

# Scroll down repeatedly
all_list = []
while True:

    html = driver.page_source
    soup = bs(html, 'html.parser')

    #
    elems = soup.find_all('a', 'production-item__overlay')
    for el in elems:
        temp = 'https://ohou.se' + el['href']
        all_list.append(temp)
    all_list = list(dict.fromkeys(all_list))

    # Scroll down by the defined amount
    driver.execute_script(f"window.scrollBy(0, {scroll_height});")
    time.sleep(5)

    # get the current scroll position
    scroll_position = driver.execute_script("return window.pageYOffset;")
    print(scroll_position)

    #마지막 페이지 확인
    if 'temp_scroll_postion' in locals() and temp_scroll_postion == scroll_position:
        print('last page')
        # print(all_list)
        print(len(all_list))

        #list_test csv파일로 저장
        with open('o_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
            write = csv.writer(f)
            write.writerows([all_list])
        break


    #아니면 계속 리스트 수집
    temp_scroll_postion = scroll_position


