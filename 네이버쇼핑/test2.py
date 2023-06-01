from datetime import datetime
from 스크롤 import *
from fake_useragent import UserAgent
import random
import requests
import pyautogui
import time

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
from selenium.webdriver.common.alert import Alert


import chromedriver_autoinstaller
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'C://Users//{path_input}//AppData//Local//Programs//Python//Python310//{chrome_ver}//chromedriver.exe'
if os.path.exists(driver_path):
    print(f"chrome driver is installed: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
chromedriver_autoinstaller.install(True)



import sh_word
import numpy as np

ua = UserAgent()
user_agents = []
for i in range(1,10):
    user_agent = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{i}{i}{i}.0.0.0 Safari/537.36'
    user_agents.append(user_agent)
user_agents = np.random.choice(user_agents)
user_agent = random.choice(user_agents)
referer = random.choice(['https://www.google.com/search','https://www.google.com/search']) # 이전 쿠키

# create Chrome options with random user agent and headers
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument(f'referer={referer}')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_options)
now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'),user_agent)




url = 'https://search.shopping.naver.com/catalog/24878389526'

# navigate to the URL
driver.get(url)
def 제품정보():
    driver.find_element(By.CLASS_NAME,'specInfo_section_title__f3VcA')
    pass

def 블로그리뷰():
    driver.find_element(By.CLASS_NAME,'specInfo_section_title__f3VcA')
    pass

def 쇼핑몰리뷰():
    driver.find_element(By.CLASS_NAME,'specInfo_section_title__f3VcA')
    pass

def AiTEMS추천():
    driver.find_element(By.CLASS_NAME,'specInfo_section_title__f3VcA')
    pass


