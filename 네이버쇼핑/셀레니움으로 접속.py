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
# driver = webdriver.Chrome(options=options)
# actions = ActionChains(driver)


import pyautogui
import time
import random

# x=50
# y=50
# cnt=0
# while True:
    
#     pyautogui.moveTo(x,y)
#     pyautogui.click(x,y)
#     print(cnt)
#     cnt+=1
#     x+=10
#     y+=10
#     print(x,y)
#     time.sleep(1)

# 일단 파이오토구이로 바로가기 버튼 누르기(좌표),  


# Loop until the element is visible
for num in range(1,101):
    
    # List of user-agent strings to randomly choose from
    user_agent_list = []
    for i in range(1,10):
        user_agent = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{i}{i}{i}.0.0.0 Safari/537.36'
        user_agent_list.append(user_agent)

    # Randomly choose a user-agent string from the list
    selected_user_agent = random.choice(user_agent_list)
    print(selected_user_agent)

    # Set the options for the Chrome browser
    options.add_argument(f'user-agent={user_agent}')

    # Start the Chrome browser with the custom user-agent
    driver = webdriver.Chrome(options=options)

    # Navigate to a webpage
    driver.get('https://search.shopping.naver.com/search/all?query=동서가구쇼파')
    while True:
        driver.execute_script('window.scrollBy(0, 100);')
        try:
            element = driver.find_element(By.PARTIAL_LINK_TEXT, '헤드레스트')
            driver.execute_script("arguments[0].scrollIntoView();", element)
            location = element.location_once_scrolled_into_view
            print(location)
            break
        except:
            continue


   

    # 네이버 쇼핑 -> 상세 페이지
    pyautogui.click(574,117) 
    time.sleep(2)

    # 상세 페이지 -> 동서 가구 몰
    pyautogui.click(770,690)
    time.sleep(random.uniform(2, 8)) # Random wait time between 2 and 5 seconds

    # switch to the second tab
    driver.switch_to.window(driver.window_handles[1])
    

    # Set the scrolling speed (in seconds)
    SCROLL_SPEED = 1

    # Set the scrolling interval (in milliseconds)
    SCROLL_INTERVAL = 100

    # Scroll to the bottom of the page
    current_scroll_position = 0
    while True:
        # Scroll down by a certain amount
        driver.execute_script("window.scrollBy(0, window.innerHeight);")
        #Wait for the page to load
        time.sleep(SCROLL_SPEED)
        
        # Check the new scroll position
        new_scroll_position = driver.execute_script("return window.pageYOffset;")
        # Stop scrolling if we've reached the bottom of the page
        if new_scroll_position == current_scroll_position:
            break
        current_scroll_position = new_scroll_position
        
        # Wait for a certain interval before scrolling down again
        time.sleep(random.uniform(2, 5))
    
    
    driver.quit()
    print(num)