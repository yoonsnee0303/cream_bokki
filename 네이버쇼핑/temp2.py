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



# '동서가구 플렉스 헤드레스트 천연 소가죽 4인 소파' 검색
# class 'basicList_link__JLQJf' click (pyautogui) # 네이버 쇼핑 -> 가구 클릭 652, 5208
# class 'productByMall_mall__SIa50' click (pyautogui) # 가구 상세페이지 -> 주식회사 동서가구 811 645
# random 초를 통해 클릭



import pyautogui
import random


# navigate to the URL
driver.get('https://search.shopping.naver.com/search/all?query=%EB%8F%99%EC%84%9C%EA%B0%80%EA%B5%AC%EC%87%BC%ED%8C%8C&')
# time.sleep(1000)

# # 네이버 쇼핑에서 가구 상세페이지 검색
# search_box = driver.find_element(By.CLASS_NAME,'_searchInput_search_text_3CUDs') # 검색창
# search_box.send_keys('동서가구 플렉스 헤드레스트 천연 소가죽 4인 소파') # 검색어 입력
# search_box.send_keys(Keys.RETURN) # enter
# time.sleep(1)

# Set the target product title
target_title = "동서가구 플렉스 헤드레스트 천연 소가죽 4인 소파"

# Scroll the page until the target title is found and get its coordinates
while True:
    try:
        # Find the element with the target text
        element = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div/div[10]/div/div/div[2]/div[1]/a')

        # Get the location of the element on the screen
        location = element.location

        # Scroll the page to the location of the element
        driver.execute_script("window.scrollTo(0, {});".format(location['y']))

        # Get the coordinates of the element on the screen
        x, y = pyautogui.position()
        x += location['x']
        y += location['y']
        
        if element.text == target_title:
            # Click on the element using pyautogui
            pyautogui.click(x=x, y=y)
            print("Target element found!")
            break
    except:
        pass

# Close the browser window
driver.quit()










# for num in range(1,101):
#     # Wait for a random time between 0 and 10 seconds
#     wait_time = random.randint(1, 8) # 랜덤 secods로 클릭하기
#     time.sleep(wait_time)

#     # 네이버 쇼핑 -> 가구 상세페이지
#     pyautogui.moveTo(750, 560) # 상세페이지 url
#     pyautogui.click()
#     time.sleep(0.5)

#     # 가구 상세 페이지 -> 동서가구 사이트
#     pyautogui.moveTo(811, 690) # 동서가구 사이트
#     pyautogui.click()
#     time.sleep(0.5)
#     pyautogui.hotkey('ctrl','w') # pyautogui로 탭 닫기(단축키)
#     print(num)

# 스크롤을 해서 '동서가구 플렉스 헤드레스트 천연 소가죽 4인 소파'를 찾아야 함! 좌표도 얻어야하고 약(609,474), text로도 가져와야하고.














# - -------------------------------------------------------------------------------------

# # try:
# #     iframe = WebDriverWait(driver, 10).until(
# #         EC.frame_to_be_available_and_switch_to_it((By.ID, 'searchIframe'))
# #     )
# # except TimeoutException:
# #     pass


# # Wait for the search box to become available and enter the search term
# search_box = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, '_searchInput_search_text_3CUDs'))
# )
# print(search_box)
# print('here')
# search_box.send_keys('소파')
# search_box.submit()

# print("일하러 갑시다")
