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
driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)

import pyautogui
import random



# set up Chrome driver
driver = webdriver.Chrome()

# navigate to the target website
driver.get('https://search.shopping.naver.com/search/all?query=%EB%8F%99%EC%84%9C%EA%B0%80%EA%B5%AC%EC%87%BC%ED%8C%8C&')


# scroll down until the target URL is found
while True:
    try:
        # find the target URL element
        target_url_elem = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div/div[10]/div/div/div[2]/div[1]/a')

        # get the location of the target URL element
        location = target_url_elem.location
        
        # print the location of the target URL element
        print("Target URL element's location: x={}, y={}".format(location['x'], location['y']))
        
        # move the cursor to the target URL element
        actions = ActionChains(driver)
        actions.move_to_element(target_url_elem)
        actions.perform()
        time.sleep(0.5)

        # move the cursor to the target URL element's location using PyAutoGUI
        pyautogui.moveTo(location['x'], location['y'])
        
        # click on the target URL element using PyAutoGUI
        pyautogui.click()
        time.sleep(0.5)

        # break out of the loop if the target URL is clicked
        break
        
    except:
        # if the target URL element is not found, scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# 스크롤을 하다가 그 글자가 나오면 멈추는거지. 그리고, 링크로 타고 들어가는거!



# Click the button using pyautogui
# pyautogui.click(x, y)

# Close the browser window
# driver.quit()

