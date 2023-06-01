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

def find_image_on_webpage(image_path, confidence_level, scroll_distance):
    browser = webdriver.Chrome()
    browser.get('https://www.gsshop.com/prd/prd.gs?prdid=90056026')
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
    pyautogui.hotkey('ctrl','shift','a')
    time.sleep(5)
    # Close the browser
    # browser.quit()

    # Return the position of the image
    return (x_pos, y_pos)


image_path = 'ds.png'
confidence_level = 0.8
scroll_distance = 180

image_position = find_image_on_webpage(image_path, confidence_level, scroll_distance)

print("Image position:", image_position)
