import time
import socket
import re
import requests
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("pwnbit.kr", 443))
in_ip = sock.getsockname()[0]
print("내부 IP: ", in_ip)
req = requests.get("http://ipconfig.kr")
ex_ip = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print("외부 IP: ", ex_ip)
# time.sleep(1000)


start_cnt = 0
if ex_ip != '183.100.232.2444':

    import csv
    #csv파일 list로 불러오기
    #csv파일 list로 불러오기
    #csv파일 list로 불러오기
    with open('gs_list.csv', 'r', newline='', encoding='utf-8-sig') as f:
        read = csv.reader(f)
        lists = list(read)
    lists = lists[0]
    print(len(lists))

    for i in range(len(lists)):

        if lists[i].count('스캔필요') + lists[i].count('패스') == 0:
            start_cnt = i
            break


    import getpass
    path_input = getpass.getuser()


    import pytesseract
    import cv2
    from matplotlib import pyplot as plt
    import urllib.request


    import pyautogui
    from bs4 import BeautifulSoup as bs
    import os
    import urllib3
    import csv
    from PIL import Image
    import sys
    import unittest
    import find_image_on_webpage
    from selenium import webdriver
    import datetime







    #이미지 내 '동서가구' 로고 포함 여부 확인
    #이미지 내 '동서가구' 로고 포함 여부 확인
    #이미지 내 '동서가구' 로고 포함 여부 확인
    def txt_check(text):
        if text.count("동서가구"):
            print(text)
            print("\n\n\n")
            return '동서가구'
        elif text.count("장인가구"):
            print(text)
            print("\n\n\n")
            return '장인가구'

    #이미지 내 '동서가구' 로고 포함 여부 확인
    #이미지 내 '동서가구' 로고 포함 여부 확인
    #이미지 내 '동서가구' 로고 포함 여부 확인
    def img_check(url):
        def 이미지확인(url):
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
            urllib.request.urlretrieve(url, "test1.jpg")
            image = cv2.imread("test1.jpg", cv2.IMREAD_GRAYSCALE) # 흑백 이미지로 로드
            img_width = int(image.shape[1])
            img_hight = int(image.shape[0])
            print(img_width, img_hight)

            print(img_width/100)
            width_unit = int(round(img_width/100))
            hight_unit = int(round(img_hight/100))
            print(width_unit)
            # plt.imshow(image, cmap="gray"), plt.axis("off")
            # plt.show()


            return image, img_width, img_hight, width_unit, hight_unit



        def 상단글자(image, width_unit, hight_unit, img_width, img_hight):
            try:
                width = 0

                print('img_width:', img_width)
                print('img_hight:', img_hight)
                print('width_unit:', width_unit)
                print('hight_unit:', hight_unit)
                # time.sleep(1000)

                for hight in range(width_unit, img_hight, hight_unit):
                    now_hight = (hight/img_hight)*50
                    print(hight)

                    if img_width != 550:
                        if hight >= 150:
                            image_cropped = image[hight-150:hight, width:]
                        else:
                            image_cropped = image[:hight, width:]
                    else :
                        if hight >= 100:
                            image_cropped = image[hight-100:hight, 300:]
                        else:
                            image_cropped = image[:hight, 300:]

                    text = pytesseract.image_to_string(image_cropped, lang='kor').strip().replace(" ", "").replace("\n","")
                    print(text)

                    # plt.imshow(image_cropped, cmap="gray"), plt.axis("off")
                    # plt.show()
                    now = datetime.datetime.now

                    if now_hight > 30:
                        return '이미지없음'
                    elif text.count('동서가구') + text.count('동셔가구') + text.count('써가구') != 0:

                        #plt.show()
                        return '동서가구'
            except:
                pass


        image, img_width, img_hight, width_unit, hight_unit = 이미지확인(url)
        check = 상단글자(image, width_unit, hight_unit, img_width, img_hight)
        print(check)

        return check











    #쿠팡 개별 상품 스캔
    #쿠팡 개별 상품 스캔
    #쿠팡 개별 상품 스캔
    def EA_cou_item_ck(url):

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


        import chromedriver_autoinstaller
        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
        driver_path = f'C:/Users/{path_input}/AppData/Local/Programs/Python/Python310\{chrome_ver}/chromedriver.exe'
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

        driver.get(url)
        time.sleep(3)
        code = driver.page_source
        soup = bs(code, 'html.parser')


        #img #img #img #img #img #img #img #img #img #img 

        #04 이미지
        def img_prc():
            img_url = soup.find('a', class_='btn_img')
            img_url = img_url.find('img')['src']
            ##
            ##
            ##
            check = img_check(img_url)
            if check == '동서가구':
                return '동서가구'

            #05 상세페이지
            detail_url = 'https://www.gsshop.com/' + soup.find('iframe', id='prdDetailIfr')['src']
            print(detail_url)

            headers = {
                'User-Agent': 'My Custom User Agent',
                'Accept-Language': 'en-US,en;q=0.5'
            }

            img_res = requests.get(detail_url, headers=headers)
            img_soup = bs(img_res.text, 'html.parser')

            elems = img_soup.find_all('img')
            for el in elems:
                img_url = el['src']
                ##
                ##
                ##
                try:
                    check = img_check(img_url)
                    if check == '동서가구':
                        break
                except:
                    pass

            driver.quit()
            if check == '동서가구':
                return '동서가구'
            else:
                return

        #img #img #img #img #img #img #img #img #img #img 



        #01 상품명
        main = soup.find('p', class_='product-title').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
        check = txt_check(main)


        #상품명이 장인가구
        if check == '장인가구':
            #구매정보 확인
            driver.find_element(By.LINK_TEXT, "구매정보").click()
            time.sleep(1)
            info_code = driver.page_source
            info_soup = bs(info_code, 'html.parser')
            info = info_soup.find('div', class_="normalN_table_wrap more").text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
            print(info)
            if info.count('동서가구'):
                return '동서가구'
            else:
                #이미지 확인
                check = img_prc()
                if check == '동서가구':
                    return '동서가구'
                else:
                    return


        #상품명이 동서가구
        elif check == '동서가구':
            #구매정보 확인
            driver.find_element(By.LINK_TEXT, "구매정보").click()
            time.sleep(1)
            info_code = driver.page_source
            info_soup = bs(info_code, 'html.parser')
            info = info_soup.find('div', class_="normalN_table_wrap more").text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
            print(info)
            if info.count('동서가구'):
                return '동서가구'
            else:
                return






    for li in range(start_cnt, len(lists)):
        check = EA_cou_item_ck(lists[li])
        if check == '동서가구':
            lists[li] = [lists[li],'스캔필요']
            #list_test csv파일로 저장
            with open('gs_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                write = csv.writer(f)
                write.writerows([lists])
        else:
            lists[li] = [lists[li],'패스']
            #list_test csv파일로 저장
            with open('gs_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                write = csv.writer(f)
                write.writerows([lists])