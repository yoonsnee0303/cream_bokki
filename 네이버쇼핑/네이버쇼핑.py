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



# 다음 검색

# Open a new Chrome window and navigate to Daum website
driver.get('https://www.daum.net//')
driver.implicitly_wait(3)


# Find the search box and type '네이버 쇼핑'
daum_search_box = driver.find_element(By.NAME,'q')
daum_search_box.send_keys('네이버쇼핑')

# Press the Enter key
daum_search_box.send_keys(Keys.ENTER)

# choose the newly tab
driver.switch_to.window(driver.window_handles[-1]) # 최근 탭 : -1
driver.implicitly_wait(3)




# 다음에서 '네이버 쇼핑' 검색
naver_search_button = driver.find_element(By.CLASS_NAME,'f_tit')
naver_search_button.click()
driver.implicitly_wait(3)

cur_url = driver.current_url # 현재 url로 드라이버 변경
print(cur_url)
driver.get(cur_url)
driver.implicitly_wait(5)


# search for '소파'
search_box = driver.find_element(By.CSS_SELECTOR,'input.co_srh_input._input')
print(driver.current_url)
driver.implicitly_wait(3)
search_box.send_keys('소파')
driver.implicitly_wait(3)
search_box.submit()

# scroll down to bottom of the page
SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# # scroll up by 100 pixels
# pyautogui.scroll(200,x=100,y=100)
# time.sleep(5)
print('스크롤 완료')




#  # 같은 이미지 찾기
# pyautogui.click('bed.png')
# time.sleep(5)

# click bed url
pyautogui.moveRel(None, 20, duration=1.5) # 상대좌표로 마우스 이동하기



# Close the browser window
# driver.quit()





# move the mouse to the top search result and click to select it
# pyautogui.moveTo(500, 500)
# pyautogui.click()

#뒤로가기 버튼 클릭하기
# driver.back()



