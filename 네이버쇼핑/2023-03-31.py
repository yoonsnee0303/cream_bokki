# 2023 - 03 - 30

import pyautogui
from pyautogui import moveTo
import time
import pyperclip
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

import chromedriver_autoinstaller
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'C://Users//{path_input}//AppData//Local//Programs//Python//Python310//{chrome_ver}//chromedriver.exe'
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

# actions = ActionChains(driver)




import pyautogui
import time
import pyperclip
from random import *
import numpy as np

start = time.time()

def ran_scl():
    return randint(1,5)

def ran_no():
    return randint(180,200)

def ran_time():
    return randint(180,200)

def scrol_dn(cnt):
    for i in range(cnt):
        pyautogui.press("down")



def open_chrome():

     # move to the window page
    pyautogui.hotkey("win","d")
    
    # Wait for the user to switch to the desired window
    time.sleep(2)

    # Press the Windows key to open the Start menu
    pyautogui.press("win")

    # Type "chrome" and press Enter to launch Google Chrome
    pyautogui.write("chrome")
    pyautogui.press("enter")

    time.sleep(0.5)

    # move to the window page
    pyautogui.hotkey("win","up")


def search_on_chrome(query):
    # Click on the address bar to activate it
    pyautogui.click(x=200, y=60)

    # Copy the query to the clipboard
    pyperclip.copy(query)

    # # Click on the address bar again to clear it and activate it
    # pyautogui.click(x=200, y=60)

    # Paste the query from the clipboard
    pyautogui.hotkey("ctrl", "v")

    # Press Enter to perform the search
    pyautogui.press("enter")
    time.sleep(5)

    # press Enter to naver_shopping
    pyautogui.click(x=276,y=324)

def click_button(x, y):
    pyautogui.click(x=x, y=y)

for i in range(1,20000):
    # randomly make an user-agent
    user_agent_list = []
    for i in range(1,10):
        user_agent = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{i}{i}{i}.0.0.0 Safari/537.36'

        user_agent_list.append(user_agent)

    # Randomly choose a user-agent string from the list
    selected_user_agent = np.random.choice(user_agent_list)
    print(selected_user_agent)

    # Set the options for the Chrome browser
    options.add_argument(f'user-agent={user_agent}')

    # Open Google Chrome
    open_chrome()

    # Search for "네이버 쇼핑"
    search_on_chrome("네이버 쇼핑")

    click_button(276,324) # 구글 -> 네이버 쇼핑 버튼 누르기
    time.sleep(1)

    click_button(492,177) # 네이버 쇼핑에서 검색창
    pyperclip.copy('동서가구 쇼파')
    time.sleep(1)

    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(1)


            


    # set the maximum number of scrolls
    max_scrolls = pyautogui.size().height // 300
    min_scrolls = 1
    element_image = 'ds.png'
    while True:
        for page in range (min_scrolls,50):
            scl_cnt = ran_scl()
            scrol_dn(scl_cnt)
            # time.sleep(0.5)
            element_location = pyautogui.locateOnScreen(element_image)
            print(element_location)

            if element_location:
                # Move the mouse to the center of the element and click to select it
                element_center = pyautogui.center(element_location)
                pyautogui.moveTo(element_center)
                pyautogui.click()
                break    
        break
    time.sleep(ran_scl())
    click_button(789,745)
    ran = ran_no()
    # ran = 5
    cnt = 0
    while True:
        cnt += 1
        scl_cnt = ran_scl()
        scrol_dn(scl_cnt)
        time.sleep(1)
        # time.sleep(ran_no())
        if ran == cnt: 
            pyautogui.hotkey('alt','f4')
            break

    print(i)
print('월요일도 파이어!!!!!!')






        








# scroll_to_element('ds') # 이미지 찾아서 스크롤 멈추기

# print("코드 실행 시간:",time.time() - start)







# 구글에서 -> 네이버 쇼핑 검색을 하고 -> '동서가구 쇼파'를 검색하고 -> 스크롤 해서 누르고 들어가고 -> 상세페이지에서 주식회사 동서가구를 선택하고 하면 되지 않을까? (770,735)
#헤더값 변경해서 주고, 

