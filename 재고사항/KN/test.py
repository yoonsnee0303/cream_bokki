from bs4 import BeautifulSoup as bs
import csv
from selenium import webdriver
import time
import requests
import urllib3
import os

#scroll down
def scroll_down(driver, scroll_amount, scroll_pause_time):
    # Get initial scroll position
    scroll_pos = driver.execute_script("return window.pageYOffset;")
    
    # Initialize variable to keep track of whether end of scroll has been reached
    end_of_scroll_reached = False

    while not end_of_scroll_reached:
        # Scroll down by scroll_amount
        driver.execute_script(f"window.scrollTo(0, {scroll_pos + scroll_amount});")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Update scroll position
        new_scroll_pos = driver.execute_script("return window.pageYOffset;")
        if new_scroll_pos == scroll_pos:
            # If scroll position hasn't changed, we've reached the end of the page
            end_of_scroll_reached = True
        else:
            # If scroll position has changed, update scroll_pos and continue scrolling
            scroll_pos = new_scroll_pos

        # If scroll position reaches the bottom, exit the function
        if scroll_pos >= driver.execute_script("return document.body.scrollHeight;") - driver.execute_script("return window.innerHeight;"):
            break

# detail_url 받아오기
def get_url():
    details_url = []
    for page in range(1,8): #(1,8)

        #url get
        url = f'https://smartstore.naver.com/kndigitalstore/category/ALL?st=POPULAR&dt=BIG_IMAGE&page={page}&size=80'

        # navigate to the URL
        res = requests.get(url)
        # parse the HTML content with bs
        soup = bs(res.text, 'html.parser')

        # find all href elements 
        elements = soup.find_all('a',class_='_3BkKgDHq3l N=a:lst.product linkAnchor')

        for element in elements:
            detail_url = 'https://smartstore.naver.com' + element['href']
            details_url.append(detail_url)
            # print(href)
    # print(len(details_url))
    # print(details_url)
    print('done')
    return details_url


# 개별상품저장
def main(details_url):

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
    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[
        0]
    driver_path = f'C:/Users/{path_input}/AppData/Local/Programs/Python/Python310\{chrome_ver}/chromedriver.exe'
    if os.path.exists(driver_path):
        print(f"chrome driver is installed: {driver_path}")
    else:
        print(f"install the chrome driver(ver: {chrome_ver})")
        chromedriver_autoinstaller.install(True)

    # 옵션 - 셀레니움
    options = webdriver.ChromeOptions()
    options.add_argument(
        "--disable-blink_features=AutomationControlled")
    options.add_experimental_option(
        "excludeSwitches", ["enable_logging"])
    options.add_argument("no_sandbox")
    options.add_argument("--start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extionsions")
    options.add_experimental_option("useAutomationExtension", False)
    # options.add_argument("headless")
    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR")
    driver = webdriver.Chrome(options=options)
    actions = ActionChains(driver)


    # details_url = https: smart~ /0000xxx
    # image url 받아오기
    cnt = 1
    for num in range(len(details_url)):
        img_url = []
        driver.get(details_url[num])
        # scroll_down(driver, 1000, 1)
        time.sleep(1)

        req=driver.page_source
        soup = bs(req,'html.parser')
        
        detail_div = soup.find_all('a', class_="se-module-image-link __se_image_link __se_link")

        for i in range(len(detail_div)):
            temp = detail_div[i].find('img')['data-src']
            img_url.append(temp)
        ck_num = [details_url[num],img_url]
        print(cnt, ck_num)
        cnt+=1

        #list_test csv파일로 계속 저장
        with open('test.csv', 'a', newline='', encoding='utf-8-sig') as f:
            write = csv.writer(f)
            write.writerows([ck_num])
        
        time.sleep(2)






    print('CSV file created successfully.')


 
#main #main #main #main #main #main #main #main #main #main 
#상품 전체 url 받아오기
details_url = get_url()
# 개별상품저장
main(details_url)