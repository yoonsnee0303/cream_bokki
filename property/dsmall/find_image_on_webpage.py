import pyautogui 
import selenium
import os
import getpass
import time
import chromedriver_autoinstaller
path_input = getpass.getuser()

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'C://Users//{path_input}//AppData//Local//Programs//Python//Python310//{chrome_ver}//chromedriver.exe'
if os.path.exists(driver_path):
    print(f"chrome driver is installed: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
chromedriver_autoinstaller.install(True)



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import datetime
now = datetime.datetime.now

def find_image_on_webpage(url,image_path):

    scroll_distance = 200
    confidence_level = 0.8 # 필요시 변경
    browser = webdriver.Chrome()
    browser.get(url)
    pyautogui.hotkey('win','up')
    x_pos, y_pos = browser.execute_script("return window.scrollX"), browser.execute_script("return window.scrollY")

    while True:
        browser.execute_script(f"window.scrollBy(0, {scroll_distance})")

        img = pyautogui.locateOnScreen(image_path, confidence=confidence_level)

        if img is not None:
            x, y, _, _ = img
            pyautogui.moveTo(x, y)
            x_pos, y_pos = pyautogui.position()
            break
    print('found image')
    time.sleep(2)
    browser.get_screenshot_as_png('gsshop/상품명/{}'.format(now))
    pyautogui.hotkey('ctrl','shift','a')
    time.sleep(5)
    return (x_pos, y_pos)


image_path = 'test1.jpg'
confidence_level = 0.8
scroll_distance = 180
url = 'https://www.ssg.com/item/itemView.ssg?itemId=1000063957210'
find_image_on_webpage(url,image_path)

print("Image position:")
