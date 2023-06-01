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
import random


# Loop until the element is visible
for num in range(1,10000):
    
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

    # Move the mouse to the coordinates and click
    pyautogui.hotkey('win','d') # 초기화면


    # set the coordinates of the link
    x = 115    
    y = 148

    # Hold down the Ctrl key and click on the link again to open it in a new window
    pyautogui.moveTo(x,y)
    pyautogui.doubleClick()
    time.sleep(2)

    # 화면 최대화
    pyautogui.hotkey('win','up')
    
   
    # 상세 페이지 -> 동서 가구 몰
    pyautogui.click(770,735)
    time.sleep(random.uniform(2, 8)) # Random wait time between 2 and 5 seconds


    # Set the amount to scroll and time between scrolls
    scroll_amount = 100
    scroll_interval = 0.5


    # Get current mouse position
    x, y = pyautogui.position()


    # Define function to scroll the webpage down
    def scroll_down():
        pyautogui.press('pagedown')


    # Loop until we've scrolled the desired amount 
    while scroll_amount > 0:
        # Scroll down
        scroll_down()
        scroll_amount -= 1
        
        # # Wait for the scroll interval
        # if i%3 == 0 : time.sleep(181)
        # elif i%3 == 1 : time.sleep(192)
        # elif i%3 == 2 : time.sleep(203)
        time.sleep(3) # 여기 수정해야함.

        pyautogui.hotkey('alt', 'f4')    

        break    

        # # Check if we've reached the end of the page
        # if pyautogui.position() == max_scroll_pos:
        
        #     # If so, close the webpage
        #     pyautogui.hotkey('ctrl', 'w')

        #     break

    # Move the mouse back to its original position
    pyautogui.moveTo(x, y)



    # closing the page
