import threading
from google.cloud import storage
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage as firebase_storage
import math

import sys
import psutil
import json
import pymysql

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget, QToolBar, QDialog
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QProgressBar, QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

from firebase_admin import storage
from firebase_admin import credentials
import firebase_admin
import requests
import re

import pytesseract
import cv2
import urllib.request
import pyautogui
from bs4 import BeautifulSoup as bs
import os
import urllib3
import csv
from PIL import Image
import unittest
import time
import socket

import datetime
now = datetime.datetime.now()
now = now.strftime('%Y%m%d %H%M%S')

import logging
from io import StringIO
import smtplib
from email.mime.text import MIMEText

import getpass
path_input = getpass.getuser()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("pwnbit.kr", 443))
in_ip = sock.getsockname()[0]
print("내부 IP: ", in_ip)
req = requests.get("http://ipconfig.kr")
ex_ip = re.search(
    r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print("외부 IP: ", ex_ip)


# Firebase 서비스 계정의 키 파일 경로
cred = credentials.Certificate(
    'upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json')

# Firebase 프로젝트 ID
project_id = 'upload-img-5b02f.appspot.com'

# Firebase 초기화
firebase_admin.initialize_app(cred, {'storageBucket': f'{project_id}'})

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
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait


import chromedriver_autoinstaller
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'C:/Users/{path_input}/AppData/Local/Programs/Python/Python310\{chrome_ver}/chromedriver.exe'
if os.path.exists(driver_path):
    print(f"chrome driver is installed: {driver_path}")
else:
    print(f"install the chrome driver(ver: {chrome_ver})")
    chromedriver_autoinstaller.install(True)



conn = pymysql.connect(host='121.254.162.132', port=3306, user='capture', password='edf@@0907', charset='utf8mb4', db='edf_capture', conv={'charset':'utf8mb4', 'use_unicode': True, 'sql_mode': 'PIPES_AS_CONCAT'})

class WorkerThread_mall(QThread):
    progress_update = pyqtSignal(int)
    log_update = pyqtSignal(str)
    log_img_update = pyqtSignal(str)
    pixmap_update = pyqtSignal(QPixmap)

    def __init__(self,test):
        super().__init__()
        self.test = test
    
    def run(self):
        import os
        import urllib3
        import getpass
        path_input = getpass.getuser()
        self.login_id = getpass.getuser()
        self.log_update.emit(f'firebase 서버 접속')


        # 옵션 - 셀레니움
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink_features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable_logging"])
        options.add_argument("no_sandbox")
        options.add_argument("--start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extionsions")
        options.add_experimental_option("useAutomationExtension", False)
        # options.add_argument("headless")
        options.add_argument("disable-gpu")
        options.add_argument("lang=ko_KR")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        options.add_argument("accept-language=ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7")

        driver = webdriver.Chrome(options=options)
        actions = ActionChains(driver)

        table_name = 'bbang_ttol'

        
        def 실행(sql_statements):
            try:
                cursor = conn.cursor()
                url_lists = []
                for sql in sql_statements:
                    cursor.execute(sql)

                    # Fetch all the rows (if app-cable)
                    rows = cursor.fetchall()

                    for row in rows:
                        # print(row)
                        url_lists.append(row[0]) # tuple로 출력되므로 [0]을 반드시 붙여야햠.
                    row_count = len(rows)
                    print("행의 개수:", row_count)
                

                # 파일저장
                # filename = 'all_list.csv'
                # import csv
                # with open(filename, 'w', newline='') as csvfile:
                #     writer = csv.writer(csvfile)
                #     writer.writerow([i[0] for i in cursor.description])  # 헤더 작성
                #     writer.writerows(rows)  # 행 작성

            finally:
                conn.close()
            
            return url_lists
            
        def 상세페이지리스트(mall):
            sql_statements = [f'select url from {table_name} where date is null And url Like "%%{mall}%%";']
            lists = 실행(sql_statements)
            print(len(lists))

            end_lists_url = lists[-1].count('스캔필요') + lists[-1].count('패스')
            if (end_lists_url== 1) :
                print(f'{mall} 브랜드 수집이 완료되었습니다.')

            # 수집이 중도에 멈췄을 경우
            else:
                for i in range(len(lists)):
                    check_cnt = lists[i].count('스캔필요') + lists[i].count('패스')
                    if check_cnt == 0:
                        start_cnt = i
                        break
            return lists, start_cnt
            
        def 패스여부(check,url):
            if check == '패스':
                sql_statements = f'UPDATE {table_name} SET status = "pass" WHERE url LIKE {url};'
            else:
                sql_statements = f'UPDATE {table_name} SET status = "nonpass" WHERE url LIKE {url};'

            실행(sql_statements)

        def 시간업데이트(url):
                sql_statements = f'UPDATE {table_name} SET start_date = current_timestamp() WHERE url LIKE {url}'
                실행(sql_statements)


        def delete_files(): #onedrive 파일 삭제

            files = os.listdir()

            for file in files:
                if  ('DESKTOP' in file):
                    if ('test1' in file):
                        os.remove(file)
                        print(f'{files.index(file)+1}/{len(files)+1}')
                    else:
                        print('삭제할 test1 파일이 없음')
                        pass
                else:
                    pass

            print('파일 확인 done')

        def open_csv(file_name):  # return lists, start_cnt

            # with open(f'{file_name}_list.csv', 'r', newline='', encoding='utf-8-sig') as f:
            #     read = csv.reader(f)
            #     lists = list(read)
            # lists = lists[0]# 중복제거
            # print(lists)

            # 수집이 모두 완료되었을 시
            end_lists_url = lists[-1].count('스캔필요') + lists[-1].count('패스')
            if (end_lists_url== 1) :
                print(f'{file_name} 브랜드 수집이 완료되었습니다.')

            # 수집이 중도에 멈췄을 경우
            else:
                for i in range(len(lists)):
                    check_cnt = lists[i].count('스캔필요') + lists[i].count('패스')
                    if check_cnt == 0:
                        start_cnt = i
                        break

            
            
            print(lists)
            print(start_cnt)
            return lists, start_cnt
        
        def brand():  # return brand_lists
            brand_lists = ['11', 'lotte', 'sin', 'naver', 'today','gmarket', 'auction', 'interpark', 'coupang']
            return brand_lists
        brand_lists = brand()

        def get_week_of_month():  # return week_syntax
            today = datetime.date.today()
            first_day_of_month = datetime.date(today.year, today.month, 1)
            week_number = (today - first_day_of_month).days // 7 + 1
            week_syntax = str(today.month) + '월' + str(week_number) + '주차'
            return week_syntax

        def delete_image(image_file_path): # 캡처 파일 삭제
            if os.path.exists(image_file_path):
                os.remove(image_file_path)
                print(f"{image_file_path}가 삭제되었습니다.")
            else:
                print(f"{image_file_path}가 존재하지 않습니다.")

        
        def txt_check(file_name, text):  # return '동서가구'
            self.log_img_update.emit(text)
            if text.count("동서가구"):
                print(text)
                print("\n\n\n")

                pyautogui.screenshot(f'{file_name}.jpg')
                image_file_path = f'{file_name}.jpg'
                # brand_lists = brand()
                for brand in brand_lists:
                    if brand in file_name:
                        # make bucket and get folder name for each brand
                        bucket = storage.bucket()
                        folder_name = get_week_of_month()
                        folder_blob = bucket.blob(folder_name)

                        # check specific folder name exist or not
                        if not folder_blob.exists():
                            print(f'Creating folder {folder_name}')
                            folder_blob.upload_from_string('')

                        # Upload a file to the folder
                        blob = bucket.blob(f'{folder_name}/{image_file_path}')
                        blob.upload_from_filename(image_file_path)
                        print(f'File {file_name} uploaded to {folder_name}')
                        self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                        delete_image(image_file_path)
                        break

                return '동서가구'
            else:
                return
            
        def img_check(url, width_con, hight_con1, hight_con2, cropped_con):  # return check, hight
            def 이미지확인(url):
                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
                
                urllib.request.urlretrieve(url, f"test1_{self.login_id}.jpg")

                # load the new pixmap
                new_pixmap = QPixmap(f"test1_{self.login_id}.jpg")

                # emit the custom signal to pass the new pixmap to the main thread
                self.pixmap_update.emit(new_pixmap)

                image = cv2.imread(f"test1_{self.login_id}.jpg", cv2.IMREAD_GRAYSCALE)  # 흑백 이미지로 로드
                # print(image)
                try:
                    if image == None:
                        return 0,0,0,0,0
                except:
                    pass
                img_width = int(image.shape[1])
                img_hight = int(image.shape[0])

                print(img_width, img_hight)
                width_unit = int(round(img_width/100))
                hight_unit = int(round(img_hight/100))

                if hight_unit == 0:
                    urllib.request.urlretrieve(url, f"test1_{getpass.getuser()}.jpg")
                    image = cv2.imread("test1.jpg", cv2.IMREAD_GRAYSCALE) # 흑백 이미지로 로드

                    img_width = int(image.shape[1])
                    img_hight = int(image.shape[0])
                    width_unit = int(round(img_width/100))
                    hight_unit = int(round(img_hight/100))
                    print('reload image')
                    print(width_unit,hight_unit)
                    return image, 
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

                    for hight in range(width_unit, img_hight, hight_unit):
                        now_hight = (hight/img_hight)*50
                        print(hight)
                        print(img_hight)

                        if img_width != width_con:
                            if hight >= hight_con1:
                                image_cropped = image[hight - hight_con1:hight, width:]
                            else:
                                image_cropped = image[:hight, width:]
                        else:
                            if hight >= hight_con2:
                                image_cropped = image[hight - hight_con2:hight, cropped_con:]
                            else:
                                image_cropped = image[:hight, cropped_con:]

                        text = pytesseract.image_to_string(image_cropped, lang='kor').strip().replace(" ", "").replace("\n", "")
                        print(text)

                        #log
                        self.log_img_update.emit(text)

                        # plt.imshow(image_cropped, cmap="gray"), plt.axis("off")
                        # plt.show()

                        if hight > (img_hight)*0.9:  # img_hight
                            return hight,img_hight,'이미지없음'
                        elif text.count('동서가구') + text.count('동셔가구') + text.count('써가구') != 0:
                            # plt.show()
                            return hight,img_hight,'동서가구'
                except:
                    return 0,0,'이미지없음'

            image, img_width, img_hight, width_unit, hight_unit = 이미지확인(url)
            hight,img_hight,check = 상단글자(image, width_unit, hight_unit, img_width, img_hight)

            return hight, img_hight, check
        
        
        try:
            # cou
            # cou
            # cou
            if self.test == '쿠팡':
                #log
                self.log_update.emit(f'firebase 서버 접속')
                if ex_ip != '183.100.232.2444':
                    lists, start_cnt = open_csv('cou') # cou_list.csv
                    brand_lists = brand()   
                    def EA_cou_item_ck(url):
                        driver.get(url)
                        time.sleep(1)
                        code = driver.page_source
                        soup = bs(code, 'html.parser')
                        pro_num = url.split('=')[1].split('&')[0]
                        file_name = 'cou' + '_' + now.split('.')[0].replace('-', '').replace(' ', '_').replace(':', '') + '_' + pro_num

                        # text #text #text #text #text #text #text #text
                        # 01 상단
                        # log
                        self.log_update.emit(f'쿠팡 [텍스트 상단] 확인 중..')
                        prod_class = soup.find('div', class_='prod-atf-main')
                        if prod_class is None:
                            print('prod_class is None')
                            return ''
                        else:
                            main = prod_class.text.strip().replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")

                        check = txt_check(file_name, main)
                        if check == '동서가구':
                            return '동서가구'
                        elif main.count('현재판매중인상품이아닙니다'):
                            print("품절 상품 / 패스")
                            return
                        
                        # 02 필수 표기정보
                        # log
                        self.log_update.emit(f'쿠팡 [텍스트 필수 표기정보] 확인 중..')
                        wait = WebDriverWait(driver, 10)  # 최대 10초 동안 기다림
                        element = wait.until(EC.presence_of_element_located((By.ID, "itemBrief")))
                        itembrief = driver.find_element(By.ID, 'itemBrief')
                        itembrief.click()
                        brief = soup.find('div', id="itemBrief").text.strip().replace (" ", "").replace("\n", "").replace("\t", "").replace("\r", "")
                        check = txt_check(file_name, brief)
                        if check == '동서가구':
                            return '동서가구'

                        # 03 배송/교환/반품 안내
                        # log
                        self.log_update.emit(f'쿠팡 [텍스트 배송/교환/반품 안내] 확인 중..')
                        driver.find_element(By.NAME, 'etc').click()
                        time.sleep(1)
                        code = driver.page_source
                        soup = bs(code, 'html.parser')
                        etc = soup.find('li', class_='product-etc tab-contents__content').text.strip().replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")
                        check = txt_check(file_name, etc)
                        if check == '동서가구':
                            return '동서가구'
                        
                        # img #img #img #img #img #img #img #img #img #img
                        # 04 이미지
                        # log
                        self.log_update.emit(f'쿠팡 [이미지 대표이미지] 확인 중..')
                        actions = ActionChains(driver)  
                        actions.send_keys(Keys.HOME).perform()  
                        img_url = 'https:' + soup.find('img', class_="prod-image__detail")['src']
                        print(img_url)
                        ##
                        ##
                        ##
                        hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                        if check == '동서가구':
                            pyautogui.screenshot(f'{file_name}.jpg')
                            print(f'{file_name}.jpg')

                            image_file_path = f'{file_name}.jpg'
                            for brand in brand_lists:

                                if brand in file_name:

                                    # make bucket and get folder name for each brand
                                    bucket = storage.bucket()
                                    folder_name = get_week_of_month()
                                    folder_blob = bucket.blob(folder_name)

                                    # check specific folder name exist or not
                                    if not folder_blob.exists():
                                        print(f'Creating folder {folder_name}')
                                        folder_blob.upload_from_string('')

                                    # Upload a file to the folder
                                    blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                    blob.upload_from_filename(image_file_path)
                                    print(f'File {file_name} uploaded to {folder_name}')
                                    self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                            return '동서가구'
                        
                        # 05 상세이미지
                        detail = soup.find('div', id="productDetail")
                        imgs = detail.find_all('img')
                        print(imgs)
                        imgs_cnt = 1
                        for img in imgs:
                            # log
                            self.log_update.emit(f'쿠팡 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                            imgs_cnt += 1
                            try:
                                src = img['src']
                                img_url = src
                                ##
                                ##
                                ##
                                hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                                if check == '동서가구':
                                    count = 0
                                    while count < len(lists):  # len(lists)
                                        img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url}']")
                                        print('find img_element')
                                        location = img_element.location
                                        print(location)
                                        img_element.click()
                                        pyautogui.screenshot(f'{file_name}.jpg')
                                        image_file_path = f'{file_name}.jpg'

                                        for brand in brand_lists:
                                            if brand in file_name:
                                                # make bucket and get folder name for each brand
                                                bucket = storage.bucket()
                                                folder_name = get_week_of_month()
                                                folder_blob = bucket.blob(folder_name)

                                                # check specific folder name exist or not
                                                if not folder_blob.exists():
                                                    print(f'Creating folder {folder_name}')
                                                    folder_blob.upload_from_string('')

                                                # Upload a file to the folder
                                                blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                                blob.upload_from_filename(image_file_path)
                                                delete_image(image_file_path)
                                                print(f'File {file_name} uploaded to {folder_name}')
                                                self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                                break
                                        break
                                    break
                            except:
                                pass
                        return check     
                print('시작', datetime.datetime.now())
                for li in range(start_cnt, len(lists)):
                    #log
                    percent = int((li+1)/(len(lists)/100))
                    self.progress_update.emit(percent)
                    lists[li] = lists[li].replace( "'", "").replace("[", "").replace("]", "")
                    self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')
                    check = EA_cou_item_ck(lists[li])
                    all_cookies = driver.get_cookies()
                    print('쿠키출력')
                    print(all_cookies)
                    driver.quit()
                    time.sleep(.5)

                    import os
                    import urllib3
                    import getpass
                    path_input = getpass.getuser()

                    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                    from selenium import webdriver as webdriver2
                    # from selenium.webdriver.common.by import By 
                    # from selenium.webdriver.common.keys import Keys
                    # from selenium.webdriver.common.action_chains import ActionChains as actionchains2

                    import chromedriver_autoinstaller as auto
                    chrome_ver = auto.get_chrome_version().split('.')[0]
                    driver_path = f'C:/Users/{path_input}/AppData/Local/Programs/Python/Python310\{chrome_ver}/chromedriver.exe'
                    if os.path.exists(driver_path):
                        print(f"chrome driver is installed: {driver_path}")
                    else:
                        print(f"install the chrome driver(ver: {chrome_ver})")
                    auto.install(True)


                    #옵션 - 셀레니움
                    options = webdriver2.ChromeOptions()
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
                    driver = webdriver2.Chrome(options=options)
                    # actions = actionchains2(driver)


                    if check == '동서가구':
                        lists[li] = [lists[li], '스캔필요']
                        with open('cou_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                            write = csv.writer(f)
                            write.writerows([lists])
                        print('스캔필요')
                        delete_image(f"test1_{getpass.getuser()}") # 로컬 test1.jpg 이미지 삭제

                        # log
                        self.log_update.emit(f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

                    else:
                        lists[li] = [lists[li], '패스']
                        # list_test csv파일로 저장
                        with open('cou_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                            write = csv.writer(f)
                            write.writerows([lists])
                        print('패스')
                        delete_image(f"test1_{getpass.getuser()}") # 로컬 test1.jpg 이미지 삭제

                        # log
                        self.log_update.emit(f'{li}/{len(lists)} // 패스\n')

                    percent = int((li+1)/(len(lists)/100))
                    # log
                    self.progress_update.emit(percent)               
                    delete_files() 
            # llst
            # llst
            # llst
            elif self.test == 'llst': 
                self.log_update.emit(f'firebase 서버 접속')
                if ex_ip != '183.100.232.2444':
                    lists, start_cnt = open_csv('11') # 11_list.csv
                    brand_lists = brand()   
                    def EA_cou_item_ck(url):
                        driver.get(url)
                        time.sleep(1)
                        code = driver.page_source
                        soup = bs(code, 'html.parser')
                        pro_num = url.split('/')[4].split('?')[0]
                        file_name = 'llst' + '_' + now.split('.')[0].replace('-', '').replace(' ', '_').replace(':', '') + '_' + pro_num

                        # text #text #text #text #text #text #text #text
                        # text #text #text #text #text #text #text #text

                        # 01 상단
                        # log
                        self.log_update.emit(f'11번가 [텍스트 상단] 확인 중..')
                        main = soup.find('div', 'l_product_side_info').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                        print(main)
                        check = txt_check(file_name,main)
                        if check == '동서가구':
                            return '동서가구'
                        elif main.count('현재판매중인상품이아닙니다'):
                            print("품절 상품 / 패스")
                            return 
                        
                        # #01 하단
                        self.log_update.emit(f'11번가 [텍스트 하단] 확인 중..')
                        element = driver.find_element(By.ID,'provisionNotice')
                        driver.execute_script("arguments[0].scrollIntoView();", element)
                        driver.execute_script("window.scrollBy(0, -100);")
                        time.sleep(.5)
                        main = element.text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                        print(main)
                        check = txt_check(file_name,main)
                        if check == '동서가구':
                            self.log_update.emit('동서가구')
                            return '동서가구'
                        elif main.count('현재판매중인상품이아닙니다'):
                            print("품절 상품 / 패스")
                            return
                        
                        
                        # img #img #img #img #img #img #img #img #img #img
                        # img #img #img #img #img #img #img #img #img #img


                        # 04 메인 이미지
                        # log
                        self.log_update.emit(f'11번가 [이미지 대표이미지] 확인 중..')
                        actions = ActionChains(driver)  
                        actions.send_keys(Keys.HOME).perform()  
                        img_url = soup.find('div', id="productImg") 
                        img_url = img_url.find('img')['src']
                        print(img_url)
                        ##
                        ##
                        ##
                        hight, img_hight, check = img_check(img_url,640,150,100,300)
                        if check == '동서가구':
                            pyautogui.screenshot(f'{file_name}.jpg')
                            image_file_path = f'{file_name}.jpg'
                            for brand in brand_lists:
                                if brand in file_name:
                                    #make bucket and get folder name for each brand
                                    bucket = storage.bucket()
                                    folder_name = get_week_of_month()
                                    folder_blob = bucket.blob(folder_name)

                                    #check specific folder name exist or not
                                    if not folder_blob.exists():
                                        print(f'Creating folder {folder_name}')
                                        folder_blob.upload_from_string('')

                                    # Upload a file to the folder
                                    blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                    blob.upload_from_filename(image_file_path)
                                    delete_image(image_file_path)
                                    print(f'File {file_name} uploaded to {folder_name}')
                                    self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                    break
                            self.log_update.emit('동서가구')
                            return '동서가구'
                        

                        # 05 상세페이지
                        self.log_update.emit(f'11번가 [이미지 상세이미지] 확인 중..')
                        iframes = driver.find_element(By.ID,'prdDescIfrm')
                        driver.switch_to.frame(iframes)
                        time.sleep(1)
                        iframe_html = driver.page_source
                        iframe_html = bs(iframe_html,'html.parser')
                        imgs = iframe_html.find_all('img')
                        print(imgs)
                        imgs_cnt = 1
                        links = []
                        for img in imgs:
                            self.log_update.emit(f'11번가 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                            imgs_cnt += 1
                            src = img['src']
                            img_url = src
                            try:

                                ##
                                ##
                                ##
                                hight, img_hight, check = img_check(img_url,640,150,100,300)
                                if check == '동서가구': 
                                    self.log_update.emit('동서가구')
                                    count = 0  

                                    while count < len(links): #lists
                                        img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url}']")
                                        print('find img_element')
                                        location = img_element.location
                                        print(location)

                                        script = "document.querySelector('.product-detail-seemore-btn').click();"
                                        time.sleep(.5)
                                        driver.execute_script(script)
                                        print(hight)
                                        driver.execute_script(f"window.scrollBy(0, {int(location['y']) - int(hight)*0.5});")
                                        time.sleep(.5)
                                        pyautogui.screenshot(f'{file_name}.jpg')
                                        image_file_path = f'{file_name}.jpg'
                                        for brand in brand_lists:
                                            if brand in file_name:
                                                #make bucket and get folder name for each brand
                                                bucket = storage.bucket()
                                                folder_name = get_week_of_month()
                                                folder_blob = bucket.blob(folder_name)

                                                #check specific folder name exist or not
                                                if not folder_blob.exists():
                                                    print(f'Creating folder {folder_name}')
                                                    folder_blob.upload_from_string('')

                                                # Upload a file to the folder
                                                blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                                blob.upload_from_filename(image_file_path)
                                                delete_image(image_file_path)
                                                print(f'File {file_name} uploaded to {folder_name}')
                                                self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                                break
                                    break
                            
                            except:
                                pass
                        return check
                print('시작', datetime.datetime.now())
                for li in range(start_cnt, len(lists)):
                    #log
                    percent = int((li+1)/(len(lists)/100))
                    self.progress_update.emit(percent)
                    lists[li] = lists[li].replace( "'", "").replace("[", "").replace("]", "")
                    self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')
                    check = EA_cou_item_ck(lists[li])

                    if check == '동서가구':
                        lists[li] = [lists[li], '스캔필요']
                        with open('11_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                            write = csv.writer(f)
                            write.writerows([lists])
                        print('스캔필요')
                        delete_image(f"test1_{getpass.getuser()}")    # 로컬 test1.jpg 이미지 삭제

                        # log
                        self.log_update.emit(f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

                    else:
                        lists[li] = [lists[li], '패스']
                        # list_test csv파일로 저장
                        with open('11_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                            write = csv.writer(f)
                            write.writerows([lists])
                        print('패스')
                        delete_image(f"test1_{getpass.getuser()}")    # 로컬 test1.jpg 이미지 삭제

                        # log
                        self.log_update.emit(f'{li}/{len(lists)} // 패스\n')

                    percent = int((li+1)/(len(lists)/100))
                    # log
                    self.progress_update.emit(percent)
                    delete_files()
            # lot
            # lot
            # lot
            elif self.test == 'lot': 
                # log
                self.log_update.emit(f'firebase 서버 접속')
                if ex_ip != '183.100.232.2444':
                    lists, start_cnt = open_csv('lot') # lot_list.csv
                    # brand_lists = brand()   
                    def EA_cou_item_ck(url):
                            driver.get(url)
                            print(url)
                            time.sleep(1)
                            scroll_height_increment = 300 
                            total_scroll_height = driver.execute_script("return document.body.scrollHeight") 

                            while True:
                                new_scroll_height = driver.execute_script("return window.pageYOffset + " + str(scroll_height_increment) + ";")
                                if new_scroll_height > total_scroll_height:
                                    new_scroll_height = total_scroll_height

                                driver.execute_script("window.scrollTo(0, " + str(new_scroll_height) + ");")

                                time.sleep(0.3)

                                if driver.execute_script("return window.pageYOffset + window.innerHeight;") >= total_scroll_height:
                                    break
                            code = driver.page_source
                            if '아쉽게도 판매하지 않는 상품입니다.' in code:
                                print('품절상품이 있습니다.')
                                return ''
                            soup = bs(code, 'html.parser')

                            pro_num = url.split('=')[1]
                            file_name = 'lotte' + '_' + now.split('.')[0].replace('-', '').replace(' ', '_').replace(':', '') + '_' + pro_num

                            # text #text #text #text #text #text #text #text
                            # 01 상단
                            # log
                            self.log_update.emit(f'롯데온 [텍스트 상단] 확인 중..')
                            main = soup.find('div', class_='purchase_product').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                            check = txt_check(file_name,main)
                            if check == '동서가구':
                                self.log_update.emit('동서가구')
                                return '동서가구'
                            elif main.count('현재판매중인상품이아닙니다'):
                                print("품절 상품 / 패스")
                                return
                            
                            # 02 구매/배송정보
                            # log
                            self.log_update.emit(f'롯데온 [구매/배송정보] 확인 중..')
                            driver.find_element(By. CLASS_NAME, 'tab2').click()
                            time.sleep(.5)
                            soup = bs(driver.page_source, 'html.parser')

                            brief = soup.find('div', class_="wrap_detail content2 on").text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                            check = txt_check(file_name,brief)
                            if check == '동서가구':
                                self.log_update.emit('동서가구')
                                return '동서가구'


                            # img #img #img #img #img #img #img #img #img #img
                            # 03 이미지
                            # log
                            self.log_update.emit(f'롯데온 [이미지 대표이미지] 확인 중..')
                            actions = ActionChains(driver)  
                            actions.send_keys(Keys.HOME).perform()  
                            thumb = soup.find('div', class_='thumb_product')
                            img_url = thumb.find('img')['src']
                            print(img_url)
                            ##
                            ##
                            ##
                            hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                            if check == '동서가구':
                                count = 0
                                while count < len(lists) : #len(lists)
                                    img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url}']")
                                    print('find img_element')
                                    location = img_element.location
                                    print(location)

                                    script = "document.querySelector('.product-detail-seemore-btn').click();"
                                    time.sleep(3)
                                    driver.execute_script(script)
                                    driver.execute_script(f"window.scrollBy(0, {location['y']}")
                                    time.sleep(2)

                                    pyautogui.screenshot(f'{file_name}.jpg')
                                    print(f'{file_name}.jpg')

                                    image_file_path = f'{file_name}.jpg'
                                    for brand in brand_lists:
                                        if brand in file_name:

                                            bucket = storage.bucket()
                                            folder_name = get_week_of_month()
                                            folder_blob = bucket.blob(folder_name)

                                            if not folder_blob.exists():
                                                print(f'Creating folder {folder_name}')
                                                folder_blob.upload_from_string('')

                                            blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                            blob.upload_from_filename(image_file_path)
                                            print(f'File {file_name} uploaded to {folder_name}')
                                            delete_image(image_file_path)
                                            break
                                    count +=1
                                return '동서가구'
                            
                            #04 상세페이지
                            self.log_update.emit(f'롯데온 [이미지 상세이미지] 확인 중..')
                            driver.find_element(By. CLASS_NAME, 'tab1').click()
                            time.sleep(1)
                            soup = bs(driver.page_source, 'html.parser')
                            detail = soup.find('div', class_="detail")
                            imgs = detail.find_all('img')
                            imgs_cnt = 1
                            for img in imgs:
                                self.log_update.emit(f'롯데온 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                                imgs_cnt += 1
                                try:
                                    src = img['src']
                                    if src.count('data:image/gif;') == 0:
                                        if src.count('https:') == 0:
                                            src = 'https:' + src
                                        img_url = src
                                        ##
                                        ##
                                        ##
                                        hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                                        if check == '동서가구':
                                            count = 0

                                            while count < len(lists) : #len(lists)
                                                img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url}']")
                                                print('find img_element')
                                                location = img_element.location
                                                print(location)

                                                script = "document.querySelector('.product-detail-seemore-btn').click();"
                                                time.sleep(1)
                                                driver.execute_script(script)
                                                driver.execute_script(f"window.scrollBy(0, {location['y']}")
                                                time.sleep(1)

                                                pyautogui.screenshot(f'{file_name}.jpg')
                                                print(f'{file_name}.jpg')

                                                image_file_path = f'{file_name}.jpg'
                                                for brand in brand_lists:
                                                    if brand in file_name:

                                                        bucket = storage.bucket()
                                                        folder_name = get_week_of_month()
                                                        folder_blob = bucket.blob(folder_name)

                                                        if not folder_blob.exists():
                                                            print(f'Creating folder {folder_name}')
                                                            folder_blob.upload_from_string('')

                                                        blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                                        blob.upload_from_filename(image_file_path)
                                                        delete_image(image_file_path)
                                                        print(f'File {file_name} uploaded to {folder_name}')
                                                        self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                                break
                                            break
                                except:
                                    pass

                            # driver.close()
                            if check == '동서가구':
                                self.log_update.emit('동서가구')
                                return '동서가구'
                            else:
                                return
                    print('시작', datetime.datetime.now())
                    for li in range(start_cnt, len(lists)):
                        #log
                        percent = int((li+1)/(len(lists)/100))
                        self.progress_update.emit(percent)
                        self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')
                        check = EA_cou_item_ck(lists[li])

                        if check == '동서가구':
                            lists[li] = [lists[li], '스캔필요']
                            with open('lot_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                                write = csv.writer(f)
                                write.writerows([lists])
                            print('스캔필요')
                            delete_image(f"test1_{getpass.getuser()}")   # 로컬 test1 이미지 삭제
                            # log
                            self.log_update.emit(f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

                        else:
                            lists[li] = [lists[li], '패스']
                            # list_test csv파일로 저장
                            with open('lot_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                                write = csv.writer(f)
                                write.writerows([lists])
                            print('패스')
                            delete_image(f"test1_{getpass.getuser()}")   # 로컬 test1 이미지 삭제
                            # log
                            self.log_update.emit(f'{li}/{len(lists)} // 패스\n')
                        
                        delete_files()
                        
            # ss
            # ss
            # ss
            elif self.test == 'ss':
                self.log_update.emit(f'firebase 서버 접속')
                if ex_ip != '183.100.232.2444':
                    lists, start_cnt = open_csv('nav') # cou_list.csv
                    # brand_lists = brand()   
                    def EA_cou_item_ck(url):
                        driver.get(url)
                        time.sleep(1)
                        code = driver.page_source
                        soup = bs(code, 'html.parser')
                        pro_num = url.split('/')[-1]
                        file_name =  'naver'+'_'+now.split('.')[0].replace('-','').replace(' ','_').replace(':','') + '_' + pro_num

                        # text #text #text #text #text #text #text #text
                        # 01 상단
                        # log
                        self.log_update.emit(f'스마트스토어 [텍스트 상단] 확인 중..')
                        main = soup.find('fieldset').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                        check = txt_check(file_name, main)
                        if check == '동서가구':
                            self.log_update.emit('동서가구')
                            return '동서가구'
                        elif main.count('현재판매중인상품이아닙니다'):
                            print("품절 상품 / 패스")
                            return
                        
                        # 02 하단
                        # log
                        self.log_update.emit(f'스마트스토어 [텍스트 하단] 확인 중..')
                        element = driver.find_element(By.CLASS_NAME,"product_info_notice")
                        driver.execute_script("arguments[0].scrollIntoView();", element)

                        main = soup.find('div', id='INTRODUCE').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")

                        check = txt_check(file_name, main)
                        if check == '동서가구':
                            self.log_update.emit('동서가구')
                            return '동서가구'
                        elif main.count('현재판매중인상품이아닙니다'):
                            print("품절 상품 / 패스")
                            return
                        
                        # img #img #img #img #img #img #img #img #img #img
                        # 03 이미지
                        # log
                        self.log_update.emit(f'스마트스토어 [이미지 대표이미지] 확인 중..')
                        actions = ActionChains(driver)  
                        actions.send_keys(Keys.HOME).perform()  
                        main = soup.find('div', id='container')
                        img_urls = main.find_all('img')
                        for imm in img_urls:
                            try:
                                if imm['alt'] == '대표이미지':
                                    img_url = imm['data-src']
                                    break
                            except:
                                pass
                        ##
                        ##
                        ##
                        hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                        if check == '동서가구':
                            count = 0
                            while count < len(lists) : 
                                
                                img_element = driver.find_element(By.XPATH, f"//img[@data-src='{img_url}']")
                                print('find img_element')
                                location = img_element.location
                                print(location)

                                driver.execute_script(f"window.scrollBy(0, {location['y']});")
                                time.sleep(1)
                                pyautogui.screenshot(f'{file_name}.jpg')
                                image_file_path = f'{file_name}.jpg'
                                        
                                for brand in brand_lists:
                                    if brand in file_name:
                                        #make bucket and get folder name for each brand
                                        bucket = storage.bucket()
                                        folder_name = get_week_of_month()
                                        folder_blob = bucket.blob(folder_name)

                                        #check specific folder name exist or not
                                        if not folder_blob.exists():
                                            print(f'Creating folder {folder_name}')
                                            folder_blob.upload_from_string('')

                                        # Upload a file to the folder
                                        blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                        blob.upload_from_filename(image_file_path)
                                        print(f'File {file_name} uploaded to {folder_name}')
                                        delete_image(image_file_path)
                                        break
                            return '동서가구'
                        
                        # 04 상세 이미지
                        # log
                        detail = soup.find('div', id='INTRODUCE')
                        imgs = detail.find_all('img')
                        imgs_cnt = 1
                        for img in imgs:
                            self.log_update.emit(f'스마트스토어 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                            imgs_cnt += 1
                            try:
                                src = img['data-src']
                                img_url = src
                                ##
                                ##
                                ##
                                hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                                if check == '동서가구':
                                    self.log_update.emit('동서가구')
                                    count = 0
                                    while count < len(lists):  # len(lists)
                                        img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url}']")
                                        print('find img_element')
                                        location = img_element.location

                                        driver.execute_script("arguments[0].scrollIntoView();", img_element) # {behavior: 'smooth', block: 'start', inline: 'nearest', aligntotop: true}
                                        time.sleep(1)
                                        pyautogui.screenshot(f'{file_name}.jpg')
                                        print(f'{file_name}.jpg')

                                        image_file_path = f'{file_name}.jpg'

                                        for brand in brand_lists:
                                            if brand in file_name:
                                                # make bucket and get folder name for each brand
                                                bucket = storage.bucket()
                                                folder_name = get_week_of_month()
                                                folder_blob = bucket.blob(folder_name)

                                                # check specific folder name exist or not
                                                if not folder_blob.exists():
                                                    print(f'Creating folder {folder_name}')
                                                    folder_blob.upload_from_string('')

                                                # Upload a file to the folder
                                                blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                                blob.upload_from_filename(image_file_path)
                                                delete_image(image_file_path)
                                                print(f'File {file_name} uploaded to {folder_name}')
                                                self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                                break
                                        break
                                    break
                            except:
                                pass
                        return check
                print('시작', datetime.datetime.now())
                for li in range(start_cnt, len(lists)):
                    #log
                    percent = int((li+1)/(len(lists)/100))
                    self.progress_update.emit(percent)
                    lists[li] = lists[li].replace( "'", "").replace("[", "").replace("]", "")
                    self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')
                    check = EA_cou_item_ck(lists[li])

                    if check == '동서가구':
                        lists[li] = [lists[li], '스캔필요']
                        with open('nav_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                            write = csv.writer(f)
                            write.writerows([lists])
                        print('스캔필요')
                        delete_image(f"test1_{getpass.getuser()}")    # 로컬 test1 이미지 삭제

                        # log
                        self.log_update.emit(f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

                    else:
                        lists[li] = [lists[li], '패스']
                        # list_test csv파일로 저장
                        with open('nav_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                            write = csv.writer(f)
                            write.writerows([lists])
                        print('패스')
                        delete_image(f"test1_{getpass.getuser()}")   # 로컬 test1 이미지 삭제
                        # log
                        self.log_update.emit(f'{li}/{len(lists)} // 패스\n')

                    percent = int((li+1)/(len(lists)/100))
                    # log
                    self.progress_update.emit(percent)       
                    delete_files()            
            # sin
            # sin
            # sin
            elif self.test == 'sin':
                self.log_update.emit(f'firebase 서버 접속')
                if ex_ip != '183.100.232.2444':
                    lists, start_cnt = open_csv('sin') # sin_list.csv
                    # 팝업 창 확인
                    def check_alert(driver):
                        try:
                            alert = Alert(driver)

                            # 경고 대화 상자의 텍스트 확인
                            popup_text = alert.text
                            print(popup_text)

                            # "품절된 상품입니다"라는 문자열이 포함되어 있는지 확인
                            if "판매가 종료된 상품입니다." in popup_text:
                                print("품절된 상품 팝업 창이 있습니다.")
                                return '판매종료'
                            else:
                                return '판매중'
                        except:
                            return '판매중'
                            

                    def EA_cou_item_ck(url):
                        
                        driver.get(url)
                        time.sleep(1)
                        check = check_alert(driver)
                            
                        if check == '판매중':
                            code = driver.page_source
                            soup = bs(code, 'html.parser')
                            pro_num = url.split('=')[1]
                            file_name = 'sin'+'_'+now.split('.')[0].replace('-','').replace(' ','_').replace(':','') + '_' + pro_num

                            # text #text #text #text #text #text #text #text
                            # 01 상단
                            # log
                            self.log_update.emit(f'신세계 [텍스트 상단] 확인 중..')
                            main = soup.find('div', 'cdtl_row_top').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                            check = txt_check(file_name, main)
                            if check == '동서가구':
                                return '동서가구'
                            elif main.count('현재판매중인상품이아닙니다'):
                                print("품절 상품 / 패스")
                                return
                            
                            # 02 필수 표기정보
                            # log
                            self.log_update.emit(f'신세계 [텍스트 필수 표기정보] 확인 중..')
                            brief = soup.find_all('div', class_="cdtl_cont_info")
                            brief_text = ''
                            i = 0
                            for br in brief:
                                brief_text = br.text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                                if str.__contains__(brief_text,'동서가구'):
                                    ActionChains(driver).move_to_element(driver.find_elements(By.CLASS_NAME,"cdtl_cont_info")[i]).perform()
                                    break
                                i += 1
                                print(i)
                            brief = brief_text
                            check = txt_check(file_name,brief)
                            if check == '동서가구':
                                self.log_update.emit('동서가구')
                                return '동서가구'
                            
                            # img #img #img #img #img #img #img #img #img #img
                            # 04 메인 이미지
                            # log
                            self.log_update.emit(f'신세계 [이미지 대표이미지] 확인 중..')

                            img_url = soup.find('span', class_='cdtl_imgbox imgzoom')
                            img_url = img_url.find('img')['src'] 
                            print(img_url)
                            ##
                            ##
                            ##
                            hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                            if check == '동서가구':
                                self.log_update.emit('동서가구')
                                pyautogui.screenshot(f'{file_name}.jpg')
                                print(f'{file_name}.jpg')

                                image_file_path = f'{file_name}.jpg'
                                for brand in brand_lists:

                                    if brand in file_name:

                                        # make bucket and get folder name for each brand
                                        bucket = storage.bucket()
                                        folder_name = get_week_of_month()
                                        folder_blob = bucket.blob(folder_name)

                                        # check specific folder name exist or not
                                        if not folder_blob.exists():
                                            print(f'Creating folder {folder_name}')
                                            folder_blob.upload_from_string('')

                                        # Upload a file to the folder
                                        blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                        blob.upload_from_filename(image_file_path)
                                        delete_image(image_file_path)
                                        print(f'File {file_name} uploaded to {folder_name}')
                                        self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                return '동서가구'
                            
                            # 05 상세 페이지
                            driver.find_element(By.CLASS_NAME,'cdtl_seller_html_collapse').click()
                            driver.find_element(By.TAG_NAME,'body').send_keys(Keys.HOME)
                            html = driver.find_element(By.CLASS_NAME,'cdtl_capture_img')
                            iframe = html.find_element(By.TAG_NAME, 'iframe')
                            driver.switch_to.frame(iframe)
                            time.sleep(1)
                            iframe_html = driver.page_source
                            iframe_html = bs(iframe_html,'html.parser')
                            imgs = iframe_html.find_all('img')
                            imgs_cnt = 1
                            for img in imgs:
                                # log
                                self.log_update.emit(f'신세계 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                                imgs_cnt += 1
                                try:
                                    src = img['src']
                                    img_url = src
                                    ##
                                    ##
                                    ##
                                    hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                                    if check == '동서가구':
                                        self.log_update.emit('동서가구')
                                        count = 0
                                        while count < len(lists):  # len(lists)
                                            img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url}']")
                                            print('find img_element')
                                            location = img_element.location
                                            print(location)
                                            img_element.click()
                                            driver.execute_script("arguments[0].scrollIntoView();", img_element)
                                            time.sleep(1)
                                            pyautogui.screenshot(f'{file_name}.jpg')
                                            print(f'{file_name}.jpg')
                                            image_file_path = f'{file_name}.jpg'
                                            for brand in brand_lists:
                                                if brand in file_name:
                                                    #make bucket and get folder name for each brand
                                                    bucket = storage.bucket()
                                                    folder_name = get_week_of_month()
                                                    folder_blob = bucket.blob(folder_name)

                                                    #check specific folder name exist or not
                                                    if not folder_blob.exists():
                                                        print(f'Creating folder {folder_name}')
                                                        folder_blob.upload_from_string('')

                                                    # Upload a file to the folder
                                                    blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                                    blob.upload_from_filename(image_file_path)
                                                    delete_image(image_file_path)
                                                    print(f'File {file_name} uploaded to {folder_name}')
                                                    self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                            count +=1
                                            break
                                        break
                                except:
                                    pass
                            return check
                    print('시작', datetime.datetime.now())
                    for li in range(start_cnt, len(lists)):
                        #log
                        percent = int((li+1)/(len(lists)/100))
                        self.progress_update.emit(percent)
                        lists[li] = lists[li].replace( "'", "").replace("[", "").replace("]", "")
                        self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')
                        check = EA_cou_item_ck(lists[li])

                        if check == '동서가구':
                            lists[li] = [lists[li], '스캔필요']
                            with open('sin_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                                write = csv.writer(f)
                                write.writerows([lists])
                            print('스캔필요')
                            delete_image(f"test1_{getpass.getuser()}")     # 로컬 test1 이미지 삭제

                            # log
                            self.log_update.emit(f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

                        else:
                            lists[li] = [lists[li], '패스']
                            # list_test csv파일로 저장
                            with open('sin_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                                write = csv.writer(f)
                                write.writerows([lists])
                            print('패스')
                            delete_image(f"test1_{getpass.getuser()}")    # 로컬 test1 이미지 삭제
                            # log
                            self.log_update.emit(f'{li}/{len(lists)} // 패스\n')

                        percent = int((li+1)/(len(lists)/100))
                        # log
                        self.progress_update.emit(percent)
                        delete_files()

            # oj
            # oj
            # oj
            elif self.test == 'oj':
                self.log_update.emit(f'firebase 서버 접속')
                if ex_ip != '183.100.232.2444':
                    lists, start_cnt = open_csv('o') # cou_list.csv
                    brand_lists = brand()   
                    def EA_cou_item_ck(url):
                        driver.get(url)
                        time.sleep(.5)
                        code = driver.page_source
                        soup = bs(code, 'html.parser')
                        string = url.split('?')[0]
                        pro_num = re.sub(r'[^0-9]', '', string)
                        file_name = 'today'+'_'+now.split('.')[0].replace('-','').replace(' ','_').replace(':','') + '_' + pro_num

                        # text #text #text #text #text #text #text #text
                        # 01 상단
                        # log
                        self.log_update.emit(f'오늘의집 [텍스트 상단] 확인 중..')
                        main = soup.find('div', 'production-selling-overview container').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                        check = txt_check(file_name, main)
                        if check == '동서가구':
                            self.log_update.emit('동서가구')
                            return '동서가구'
                        elif main.count('현재판매중인상품이아닙니다'):
                            print("품절 상품 / 패스")
                            return
                        
                        # img #img #img #img #img #img #img #img #img #img
                        # 04 메인 이미지
                        # log
                        self.log_update.emit(f'오늘의집 [이미지 대표이미지] 확인 중..')
                        actions = ActionChains(driver)  
                        actions.send_keys(Keys.HOME).perform()  
                        img_url = soup.find('img', class_="production-selling-cover-image__entry__image")['src']
                        print(img_url)
                        ##
                        ##
                        ##
                        hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                        if check == '동서가구':
                            self.log_update.emit('동서가구')
                            pyautogui.screenshot(f'{file_name}.jpg')
                            print(f'{file_name}.jpg')
                            image_file_path = f'{file_name}.jpg'
                            for brand in brand_lists:

                                if brand in file_name:

                                    # make bucket and get folder name for each brand
                                    bucket = storage.bucket()
                                    folder_name = get_week_of_month()
                                    folder_blob = bucket.blob(folder_name)

                                    # check specific folder name exist or not
                                    if not folder_blob.exists():
                                        print(f'Creating folder {folder_name}')
                                        folder_blob.upload_from_string('')

                                    # Upload a file to the folder
                                    blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                    blob.upload_from_filename(image_file_path)
                                    print(f'File {file_name} uploaded to {folder_name}')
                                    delete_image(image_file_path)
                                    self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                            return '동서가구'
                        
                        # 04 상세이미지

                        detail = soup.find('div', class_="production-selling-description__content")
                        try:
                            imgs = detail.find_all('img')
                        except:
                            return ''
                        # print(imgs)
                        go_out = False
                        imgs_cnt = 1
                        for img in imgs:
                            # log
                            self.log_update.emit(f'오늘의집 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                            imgs_cnt += 1
                            try:
                                src = img['src']
                                img_url = src
                                ##
                                ##
                                ##
                                hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                                if check == '동서가구':
                                    detail = soup.find('div', class_="production-selling-description__content")
                                    imgs = detail.find_all('img')
                                    self.log_update.emit('동서가구')
                                    for img in imgs:
                                        src = img['src']
                                        img_url2 = src
                                        img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url2}']")
                                        driver.execute_script("arguments[0].scrollIntoView(true);", img_element)
                                        time.sleep(.5)
                                        scroll_y = driver.execute_script('return window.scrollY;')


                                        if img_url == img_url2:
                                            go_out = True
                                            if img_hight < 300:
                                                driver.execute_script(f'window.scrollTo(0, {str(int(scroll_y)-int(img_hight*2))});')
                                            elif hight > 800:
                                                hight = hight*.7
                                                driver.execute_script(f'window.scrollTo(0, {str(int(scroll_y)+int(hight))});')
                                            time.sleep(2)

                                            print('scroll_y', scroll_y)
                                            print('hight', hight)
                                            print('img_hight', img_hight)

                                            pyautogui.screenshot(f'{file_name}_img.jpg')
                                            print(f'{file_name}_img.jpg')

                                            image_file_path = f'{file_name}_img.jpg'
                                            for brand in brand_lists:
                                                if brand in file_name:

                                                    #make bucket and get folder name for each brand
                                                    bucket = storage.bucket()
                                                    folder_name = get_week_of_month()
                                                    folder_blob = bucket.blob(folder_name)

                                                    #check specific folder name exist or not
                                                    if not folder_blob.exists():
                                                        print(f'Creating folder {folder_name}')
                                                        folder_blob.upload_from_string('')

                                                    # Upload a file to the folder
                                                    blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                                    blob.upload_from_filename(image_file_path)
                                                    delete_image(image_file_path)
                                                    print(f'File {file_name} uploaded to {folder_name}')
                                                    self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                                    break
                                        if go_out == True:
                                            break
                                if go_out == True:
                                    break
                            except:
                                pass
                        return check
                print('시작', datetime.datetime.now())
                for li in range(start_cnt, len(lists)):
                    #log
                    percent = int((li+1)/(len(lists)/100))
                    self.progress_update.emit(percent)
                    lists[li] = lists[li].replace( "'", "").replace("[", "").replace("]", "")
                    self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')
                    check = EA_cou_item_ck(lists[li])

                    if check == '동서가구':
                        lists[li] = [lists[li], '스캔필요']
                        with open('o_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                            write = csv.writer(f)
                            write.writerows([lists])
                        print('스캔필요')
                        delete_image(f"test1_{getpass.getuser()}")    # 로컬 test1 이미지 삭제

                        # log
                        self.log_update.emit(f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

                    else:
                        lists[li] = [lists[li], '패스']
                        # list_test csv파일로 저장
                        with open('o_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                            write = csv.writer(f)
                            write.writerows([lists])
                        print('패스')
                        delete_image(f"test1_{getpass.getuser()}")   # 로컬 test1 이미지 삭제 
                        # log
                        self.log_update.emit(f'{li}/{len(lists)} // 패스\n')

                    percent = int((li+1)/(len(lists)/100))
                    # log
                    self.progress_update.emit(percent)
                    delete_files()
            # interpark
            # interpark
            # interpark
            elif self.test == 'interpark':
                self.log_update.emit(f'firebase 서버 접속')
                if ex_ip != '183.100.232.2444':
                    lists, start_cnt = open_csv('inter') # inter_list.csv
                    def check_alert(driver):
                        try:
                            alert = Alert(driver)
                            # 경고 대화 상자의 텍스트 확인
                            popup_text = alert.text
                            print(popup_text)

                            # "품절된 상품입니다"라는 문자열이 포함되어 있는지 확인
                            if "상품정보를 조회할 수 없습니다." in popup_text:
                                print("품절된 상품 팝업 창이 있습니다.")
                                return '판매종료'
                            else:
                                return '판매중'
                        except:
                            return '판매중'
                    def EA_cou_item_ck(url):
                        driver.get(url)
                        time.sleep(.5)
                        try:
                            alert = Alert(driver)
                            popup_text = alert.text
                            if '상품정보를 조회할 수 없습니다.' in popup_text:
                                alert.accept()
                                time.sleep(.5)
                                return ''
                        except:
                            pass

                        # check = check_alert
                        # if check == '판매종료':
                        #     print('ck2')
                        #     return ''
                        code = driver.page_source
                        soup = bs(code, 'html.parser')
                        pro_num = url.split("=")[1]
                        file_name = 'interpark'+'_'+now.split('.')[0].replace('-','').replace(' ','_').replace(':','') + '_' + pro_num

                        # text #text #text #text #text #text #text #text
                        # 01 상단
                        # log
                        self.log_update.emit(f'인터파크 [텍스트 상단] 확인 중..')
                        main = soup.find('div', 'productTopRight').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                        check = txt_check(file_name, main)
                        if check == '동서가구':
                            self.log_update.emit('동서가구')
                            return '동서가구'
                        elif main.count('현재판매중인상품이아닙니다'):
                            print("품절 상품 / 패스")
                            return
                        
                        
                        # img #img #img #img #img #img #img #img #img #img
                        # 04 이미지
                        # log
                        self.log_update.emit(f'인터파크 [이미지 대표이미지] 확인 중..')
                        actions = ActionChains(driver)  
                        actions.send_keys(Keys.HOME).perform()  
                        img_url = soup.find('div', class_='viewImage')
                        img_url = img_url.find('img')['src']
                        print(img_url)
                        ##
                        ##
                        ##
                        hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                        if check == '동서가구':
                            pyautogui.screenshot(f'{file_name}.jpg')
                            print(f'{file_name}.jpg')

                            image_file_path = f'{file_name}.jpg'
                            for brand in brand_lists:
                                if brand in file_name:
                                    # make bucket and get folder name for each brand
                                    bucket = storage.bucket()
                                    folder_name = get_week_of_month()
                                    folder_blob = bucket.blob(folder_name)

                                    # check specific folder name exist or not
                                    if not folder_blob.exists():
                                        print(f'Creating folder {folder_name}')
                                        folder_blob.upload_from_string('')

                                    # Upload a file to the folder
                                    blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                    blob.upload_from_filename(image_file_path)
                                    delete_image(image_file_path)
                                    print(f'File {file_name} uploaded to {folder_name}')
                                    self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                            return '동서가구'
                        

                        # 05. 상세이미지
                        iframes = driver.find_elements(By.TAG_NAME, "iframe")
                        print(len(iframes))
                        for ifr in iframes:
                            if ifr.get_attribute('title').count('상품상세') > 0:
                                driver.switch_to.frame(ifr)
                                detail2 = bs(driver.page_source, 'html.parser')
                                break
                        
                        imgs = detail2.find_all('img')
                        go_out = False
                        imgs_cnt = 1
                        for img in imgs:
                            # log
                            self.log_update.emit(f'인터파크 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                            imgs_cnt += 1
                            try:
                                src = img['src']
                                img_url = src
                                ##
                                ##
                                ##
                                hight, img_hight, check = img_check(img_url,640,150,100,300)
                                if check == '동서가구':
                                    detail3 = bs(driver.page_source, 'html.parser')
                                    imgs = detail3.find_all('img')

                                    for img in imgs:
                                        src = img['src']
                                        img_url2 = src
                                        img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url2}']")
                                        img_element.click()

                                        # driver.execute_script("arguments[0].scrollIntoView(true);", img_element)
                                        time.sleep(.5)
                                        scroll_y = driver.execute_script('return window.scrollY;')


                                        if img_url == img_url2:
                                            go_out = True
                                            if img_hight < 300:
                                                driver.execute_script(f'window.scrollTo(0, {str(int(scroll_y)-int(img_hight*2))});')
                                            elif hight > 800:
                                                hight = hight*.7
                                                driver.execute_script(f'window.scrollTo(0, {str(int(scroll_y)+int(hight))});')
                                            time.sleep(.5)

                                            print('scroll_y', scroll_y)
                                            print('hight', hight)
                                            print('img_hight', img_hight)
                                            
                                            pyautogui.screenshot(f'{file_name}.jpg')
                                            print(f'{file_name}.jpg')

                                            image_file_path = f'{file_name}.jpg'
                                            for brand in brand_lists:
                                                if brand in file_name:

                                                    #make bucket and get folder name for each brand
                                                    bucket = storage.bucket()
                                                    folder_name = get_week_of_month()
                                                    folder_blob = bucket.blob(folder_name)

                                                    #check specific folder name exist or not
                                                    if not folder_blob.exists():
                                                        print(f'Creating folder {folder_name}')
                                                        folder_blob.upload_from_string('')

                                                    # Upload a file to the folder
                                                    blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                                    blob.upload_from_filename(image_file_path)
                                                    delete_image(image_file_path)
                                                    print(f'File {file_name} uploaded to {folder_name}')
                                                    self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                                    break
                                        if go_out == True:
                                            break
                                if go_out == True:
                                    break
                            except:
                                pass
                        return check
                print('시작', datetime.datetime.now())
                for li in range(start_cnt, len(lists)):
                    #log
                    percent = int((li+1)/(len(lists)/100))
                    self.progress_update.emit(percent)
                    lists[li] = lists[li].replace( "'", "").replace("[", "").replace("]", "")
                    self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')
                    check = EA_cou_item_ck(lists[li])

                    if check == '동서가구':
                        lists[li] = [lists[li], '스캔필요']
                        with open('inter_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                            write = csv.writer(f)
                            write.writerows([lists])
                        print('스캔필요')
                        delete_image(f"test1_{getpass.getuser()}")    # 로컬 test1 이미지 삭제

                        # log
                        self.log_update.emit(f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

                    else:
                        lists[li] = [lists[li], '패스']
                        # list_test csv파일로 저장
                        with open('inter_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                            write = csv.writer(f)
                            write.writerows([lists])
                        print('패스')
                        delete_image(f"test1_{getpass.getuser()}")    # 로컬 test1 이미지 삭제
                        # log
                        self.log_update.emit(f'{li}/{len(lists)} // 패스\n')

                    percent = int((li+1)/(len(lists)/100))
                    # log
                    self.progress_update.emit(percent)
                    delete_files()
            # auction
            # auction
            # auction
            elif self.test == 'auction':
                self.log_update.emit(f'firebase 서버 접속')
                if ex_ip != '183.100.232.2444':
                    #####
                    lists,start_cnt = 상세페이지리스트('auction')

                    # brand_lists = brand()   
                    def EA_cou_item_ck(url):
                        driver.get(url)
                        time.sleep(.5)
                        #####
                        시간업데이트(url)
                        current_url = driver.current_url

                        # error # error # error # error # errror
                        if 'redirect=1' in current_url:
                            time.sleep(1)
                            print(url)
                            driver.get(url)

                        code = driver.page_source
                        soup = bs(code, 'html.parser')
                        pro_num = url.split('=')[1]
                        file_name = 'auction' + '_' + now.split('.')[0].replace('-', '').replace(' ', '_').replace(':', '') + '_' + pro_num

                        # text #text #text #text #text #text #text #text
                        # 01 상단
                        # log
                        self.log_update.emit(f'옥션 [텍스트 상단] 확인 중..')
                        main = soup.find('div', 'item-topinfo').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                        check = txt_check(file_name, main)
                        if check == '동서가구':
                            return '동서가구'
                        elif main.count('현재판매중인상품이아닙니다'):
                            print("품절 상품 / 패스")
                            return
                        

                        # img #img #img #img #img #img #img #img #img #img
                        # 04 이미지
                        # log
                        button = driver.find_element(By.CLASS_NAME, "button__detail-more.js-toggle-button")
                        button.click()
                        img_url = soup.find('div', class_='box__viewer-container')
                        img_url = 'https:' + img_url.find('img')['src'] 
                        print(img_url)
                        ##
                        ##
                        ##
                        hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                        if check == '동서가구':
                            pyautogui.screenshot(f'{file_name}.jpg')
                            print(f'{file_name}.jpg')

                            image_file_path = f'{file_name}.jpg'
                            for brand in brand_lists:

                                if brand in file_name:

                                    # make bucket and get folder name for each brand
                                    bucket = storage.bucket()
                                    folder_name = get_week_of_month()
                                    folder_blob = bucket.blob(folder_name)

                                    # check specific folder name exist or not
                                    if not folder_blob.exists():
                                        print(f'Creating folder {folder_name}')
                                        folder_blob.upload_from_string('')

                                    # Upload a file to the folder
                                    blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                    blob.upload_from_filename(image_file_path)
                                    delete_image(image_file_path)
                                    print(f'File {file_name} uploaded to {folder_name}')
                                    self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                    
                            return '동서가구'
                        
                        # 05 상세이미지
                        iframe = driver.find_element(By.ID,'hIfrmExplainView')
                        driver.switch_to.frame(iframe)
                        time.sleep(2)
                        iframe_html = driver.page_source
                        iframe_html = bs(iframe_html,'html.parser')
                        imgs = iframe_html.find_all('img')
                        print(imgs)

                        imgs_cnt = 1
                        for img in imgs:
                            # log
                            self.log_update.emit(f'옥션 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                            imgs_cnt += 1
                            try:
                                src = img['src']
                                img_url = src
                                ##
                                ##
                                ##

                                hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                                if check == '동서가구':
                                    count = 0
                                    while count < len(lists):  # len(lists)
                                        img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url}']")
                                        print('find img_element')
                                        location = img_element.location
                                        print(location)
                                        time.sleep(.5)
                                        img_element.click()
                                        driver.execute_script(f"window.scrollBy(0,{int(location['y']) - int(hight)*0.5});")
                                        time.sleep(2)
                                        pyautogui.screenshot(f'{file_name}.jpg')
                                        print(f'{file_name}.jpg')
                                        image_file_path = f'{file_name}.jpg'
                                        for brand in brand_lists:
                                            if brand in file_name:
                                                #make bucket and get folder name for each brand
                                                bucket = storage.bucket()
                                                folder_name = get_week_of_month()
                                                folder_blob = bucket.blob(folder_name)

                                                #check specific folder name exist or not
                                                if not folder_blob.exists():
                                                    print(f'Creating folder {folder_name}')
                                                    folder_blob.upload_from_string('')

                                                # Upload a file to the folder
                                                blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                                blob.upload_from_filename(image_file_path)
                                                delete_image(image_file_path)
                                                print(f'File {file_name} uploaded to {folder_name}')
                                                self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                        count +=1
                                        break
                                    break
                            except:
                                pass
                        return check
                print('시작', datetime.datetime.now())
                for li in range(start_cnt, len(lists)):
                    #log
                    percent = int((li+1)/(len(lists)/100))
                    self.progress_update.emit(percent)
                    lists[li] = lists[li].replace( "'", "").replace("[", "").replace("]", "")
                    self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')
                    check = EA_cou_item_ck(lists[li])
                    패스여부(check,lists[li])
                    print('done')
                    print('done')
                    print('done')
                    print('done')
                    print('done')

                    print(lists[li])
                    time.sleep(1000)

                    # if check == '동서가구':
                    #     lists[li] = [lists[li], '스캔필요']
                    #     with open('auc_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                    #         write = csv.writer(f)
                    #         write.writerows([lists])
                    #     print('스캔필요')
                    #     delete_image(f"test1_{getpass.getuser()}")    

                    #     # log
                    #     self.log_update.emit(f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

                    # else:
                    #     lists[li] = [lists[li], '패스']
                    #     # list_test csv파일로 저장
                    #     with open('auc_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                    #         write = csv.writer(f)
                    #         write.writerows([lists])
                    #     print('패스')
                    #     delete_image(f"test1_{getpass.getuser()}")    
                    #     # log
                    #     self.log_update.emit(f'{li}/{len(lists)} // 패스\n')

                    percent = int((li+1)/(len(lists)/100))
                    # log
                    self.progress_update.emit(percent)
                    delete_files()
            # gmarket
            # gmarket
            # gmarket
            elif self.test == 'gmarket':
                self.log_update.emit(f'firebase 서버 접속')
                if ex_ip != '183.100.232.2444':
                    lists, start_cnt = open_csv('gm') # cou_list.csv
                    # brand_lists = brand()   
                    def EA_cou_item_ck(url):
                        driver.get(url)
                        time.sleep(1)
                        code = driver.page_source
                        soup = bs(code, 'html.parser')
                        pro_num = url.split('=')[1]
                        file_name = 'gmarket' + '_' + now.split('.')[0].replace('-', '').replace(' ', '_').replace(':', '') + '_' + pro_num

                        # text #text #text #text #text #text #text #text
                        # 01 상단
                        # log
                        self.log_update.emit(f'지마켓 [텍스트 상단] 확인 중..')
                        main = soup.find('div', 'item-topinfo').text.strip().replace(" ", "").replace("\n","").replace("\t","").replace("\r","")
                        check = txt_check(file_name, main)
                        if check == '동서가구':
                            return '동서가구'
                        elif main.count('현재판매중인상품이아닙니다'):
                            print("품절 상품 / 패스")
                            return
                        

                        # img #img #img #img #img #img #img #img #img #img
                        # 04 이미지
                        # log
                        self.log_update.emit(f'지마켓 [이미지 대표이미지] 확인 중..')
                        actions = ActionChains(driver)  
                        actions.send_keys(Keys.HOME).perform()  
                        img_url = soup.find('div', class_="box__viewer-container")
                        img_url = img_url.find('img')['src']
                        print(img_url)

                        ##
                        ##
                        ##
                        hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                        if check == '동서가구':
                            pyautogui.screenshot(f'{file_name}.jpg')
                            print(f'{file_name}.jpg')

                            image_file_path = f'{file_name}.jpg'
                            for brand in brand_lists:

                                if brand in file_name:

                                    # make bucket and get folder name for each brand
                                    bucket = storage.bucket()
                                    folder_name = get_week_of_month()
                                    folder_blob = bucket.blob(folder_name)

                                    # check specific folder name exist or not
                                    if not folder_blob.exists():
                                        print(f'Creating folder {folder_name}')
                                        folder_blob.upload_from_string('')

                                    # Upload a file to the folder
                                    blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                    blob.upload_from_filename(image_file_path)
                                    delete_image(image_file_path)
                                    print(f'File {file_name} uploaded to {folder_name}')
                                    self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                            return '동서가구'
                        
                        # 05 상세이미지
                        iframes = driver.find_element(By.XPATH,"//iframe[@id='detail1']")
                        driver.switch_to.frame(iframes)
                        time.sleep(2)
                        iframe_html = driver.page_source
                        iframe_html = bs(iframe_html,'html.parser')
                        imgs = iframe_html.find_all('img')
                        print(imgs)

                        imgs_cnt = 1
                        for img in imgs:
                            # log
                            self.log_update.emit(f'지마켓 [이미지 상세이미지] 확인 중 ({imgs_cnt}/{len(imgs)})..')
                            imgs_cnt += 1
                            try:
                                src = img['src']
                                img_url = src
                                ##
                                ##
                                ##
                                hight, img_hight, check = img_check(img_url, 640, 150, 100, 300)
                                if check == '동서가구':
                                    count = 0
                                    while count < len(lists):  # len(lists)
                                        img_element = driver.find_element(By.XPATH, f"//img[@src='{img_url}']")
                                        print('find img_element')
                                        location = img_element.location
                                        print(location)

                                        script = "document.querySelector('.product-detail-seemore-btn').click();"
                                        time.sleep(3)
                                        driver.execute_script(script)
                                        driver.execute_script(f"window.scrollBy(0, {location['y']}")
                                        time.sleep(2)
                                        pyautogui.screenshot(f'{file_name}.jpg')
                                        image_file_path = f'{file_name}.jpg'

                                        for brand in brand_lists:
                                            if brand in file_name:

                                                #make bucket and get folder name for each brand
                                                bucket = storage.bucket()
                                                folder_name = get_week_of_month()
                                                folder_blob = bucket.blob(folder_name)

                                                #check specific folder name exist or not
                                                if not folder_blob.exists():
                                                    print(f'Creating folder {folder_name}')
                                                    folder_blob.upload_from_string('')

                                                # Upload a file to the folder
                                                blob = bucket.blob(f'{folder_name}/{image_file_path}')
                                                blob.upload_from_filename(image_file_path)
                                                delete_image(image_file_path)
                                                print(f'File {file_name} uploaded to {folder_name}')
                                                self.log_update.emit(f'File {file_name} uploaded to {folder_name}')
                                        count +=1
                                        break
                                    break
                            except:
                                pass
                        return check
                    print('시작', datetime.datetime.now())
                for li in range(start_cnt, len(lists)):
                    #log
                    percent = int((li+1)/(len(lists)/100))
                    self.progress_update.emit(percent)
                    lists[li] = lists[li].replace( "'", "").replace("[", "").replace("]", "")
                    self.log_update.emit(f'{li}/{len(lists)} 스캔시작...')
                    check = EA_cou_item_ck(lists[li])

                if check == '동서가구':
                    self.log_update.emit('동서가구')
                    lists[li] = [lists[li], '스캔필요']
                    with open('gm_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('스캔필요')
                    delete_image(f"test1_{getpass.getuser()}")        

                    # log
                    self.log_update.emit(f'{li}/{len(lists)} // 캡쳐 및 서버 전송 완료\n')

                else:
                    lists[li] = [lists[li], '패스']
                    # list_test csv파일로 저장
                    with open('gm_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
                        write = csv.writer(f)
                        write.writerows([lists])
                    print('패스')
                    delete_image(f"test1_{getpass.getuser()}")        

                    # log
                    self.log_update.emit(f'{li}/{len(lists)} // 패스\n')

                percent = int((li+1)/(len(lists)/100))
                # log
                self.progress_update.emit(percent)        
                delete_files()
        except Exception as e:
            # 예외 로그 기록
            logging.exception("예외 발생! ")

            error_buffer = StringIO()
            error_logs = error_buffer .getvalue()

            smtp = smtplib.SMTP('smtp.gmail.com', 587)

            smtp.ehlo()

            smtp.starttls()

            smtp.login('yoonsnee0303@gmail.com', 'qazyvibmpygpzswl')

            msg = MIMEText(error_logs) # 텍스트 내용
            msg['Subject'] = getpass.getuser() + '_' + error_logs # 제목

            # 다중 이메일 보낼 때
            # list = ['tw04013@naver.com','gijungcpy@gmail.com'] 
            # for mail in list:
            smtp.sendmail('yoonsnee0303@gmail.com', 'yoonsnee0303@gmail.com', msg.as_string()) # 본인한테 메일보내기
            print('error send email')

            smtp.quit()

class WorkerThread_list_get(QThread):
    progress_update = pyqtSignal(int)
    log_update = pyqtSignal(str)
    log_update2 = pyqtSignal(str)

    def run(self):
        def sql_proc(sql_statements):
            # Execute each SQL statement separately
            for sql in sql_statements:
                conn = pymysql.connect(host='121.254.162.132', port=3306, user='capture', password='edf@@0907', charset='utf8mb4', db='edf_capture', conv={'charset':'utf8mb4', 'use_unicode': True, 'sql_mode': 'PIPES_AS_CONCAT'})
            # Create a cursor object
                cursor = conn.cursor()
                cursor.execute(sql)

                # Fetch all the rows (if app-cable)
                rows = cursor.fetchall()
                cursor.close()
                conn.close()

                # Print the fetched rows
                # for row in rows:
                #     print(row)


        def get_week():
            # def get_week_of_month(date):
            #     first_day = date.replace(day=1)
            #     adjusted_day = first_day + datetime.timedelta(days=(6 - first_day.weekday()))
            #     week_number = (date - adjusted_day).days // 7 + 2
            #     return week_number

            # 현재 날짜 구하기

            def current_month_weeks():
                current_date = datetime.date.today()
                # current_date = datetime.date(2023, 8, 20)  # test test test 

                start_date = datetime.date(current_date.year, current_date.month, 1)
                end_date = start_date + datetime.timedelta(days=31)
                
                current_week = 1
                week_to_check = (current_date.day - 1) // 7 + 1  # 현재 날짜가 속한 주차 계산
                is_in_week = False
                
                while start_date < end_date:
                    if start_date.month != current_date.month:
                        break
                        
                    if current_week == week_to_check:
                        is_in_week = True
                        break
                    
                    start_date += datetime.timedelta(weeks=1)
                    current_week += 1
                
                if is_in_week:
                    date = f"{start_date.strftime('%m월')} {week_to_check}주차"
                return date
            date = current_month_weeks()
            # Firebase Storage 인스턴스 생성
            bucket = firebase_storage.bucket()

            blobs = bucket.list_blobs()
            for blob in blobs:
                # print(blob.name)
                folder_name = blob.name.split('/')[0]
                if date == folder_name:
                    print(f'{date}는 이미 다운로드 되어있는 주차입니다.')
                    return date,'다운로드 필요없음'
            return date,'다운로드 필요'
        
        def get_list(date):
            brand_lists = ['11', 'lotte', 'naver', 'today', 'sin','gmarket', 'auction', 'interpark','coupang'] 
            # brand_lists = ['interpark'] 

            # brand_lists = ['coupang']
            cnt = 1
            ratio = 11
            for brand in brand_lists:
                if brand == '11':
                    self.log_update.emit("11번가")
                    json_data = []
                    for pg in range(1,9): #41
                        test = int((ratio/8)*pg)
                        self.progress_update.emit(test)

                        url = f'https://search.11st.co.kr/Search.tmall?method=getSearchFilterAjax&kwd=동서가구+장인가구&pageNo={pg}&pageSize=250'
                        response = requests.get(url)
                        response_json = response.json()  # JSON 형식으로 변환
                        ll_cnt = 1
                        for i in range(len(response_json['commonPrdList']['items'])):

                            # 상세페이지 url
                            u = response_json['commonPrdList']['items'][i]['productDetailUrl']

                            # save sql db
                            sql_statements = [f"insert into bbang_ttol (url) values ('{u}');"]
                            sql_proc(sql_statements)
                            print(f"11번가 {ll_cnt}")

                            # log
                            self.log_update2.emit(f"상세페이지 총 {ll_cnt}개 수집")
                            ll_cnt += 1

                    self.log_update2.emit(f"{date} csv 파일 저장 완료")
                    print(f'{date} 상세페이지 파일 업로드')

                elif brand == 'lotte':
                    self.log_update.emit("롯데온")
                    url = 'https://www.lotteimall.com/search/searchMain.lotte?isTemplate=Y&headerQuery=장인가구&colldisplay=3200'
                    response = requests.get(url)
                    json_data = response.json()
                    temp = json_data['body'][16]['data'] # 15 or 16
                    # print(len(temp))
                    lotte_cnt = 1
                    for i in range(len(temp)):
                        test = int((ratio/len(temp))*i+ratio*1)

                        # log
                        self.progress_update.emit(test)

                        # 상세페이지 url
                        url = 'https://www.lotteimall.com/goods/viewGoodsDetail.lotte?goods_no=' + str(temp[i]['wishListMap']['goods_no'])

                        # save sql db
                        sql_statements = [f"insert into bbang_ttol (url) values ('{url}');"]
                        sql_proc(sql_statements)
                        

                        # log
                        print(f'롯데온 {lotte_cnt}')
                        self.log_update2.emit(f"상세페이지 총 {lotte_cnt}개 수집")
                        lotte_cnt += 1

                    self.log_update2.emit(f"{date} csv 파일 저장 완료")
                    print(f'{date} 상세페이지 파일 업로드')

                elif brand == 'naver':
                    self.log_update.emit("스마트스토어")
                    find_word = '/newdf2013/products/'
                    for page in range(1, 23):
                        test = int((ratio/22)*page+ratio*2)
                        self.progress_update.emit(test)
                        url = f'https://smartstore.naver.com/newdf2013/category/e78c2895503c4c4e993a71348c4cd9e8?st=POPULAR&dt=IMAGE&page={page}&size=40'
                        res = requests.get(url)
                        html = res.text
                        cnt = html.count(find_word)
                        
                        naver_cnt = 1
                        for i in range(cnt):
                            html = html[html.find(find_word)+len(find_word):]

                            # 상세페이지 url
                            ea_url = 'https://smartstore.naver.com/newdf2013/products/' + html[:html.find('"')]

                            # save sql db
                            sql_statements = [f"insert into bbang_ttol (url) values ('{ea_url}');"]
                            sql_proc(sql_statements)

                            # log
                            self.log_update2.emit(f"상세페이지 총 {naver_cnt}개 수집")
                            print(f'스마트스토어 {naver_cnt}')
                            print(ea_url)

                    # log
                    self.log_update2.emit(f"{date} 상세페이지 ")
                    print(f'{date} 상세페이지 파일 업로드')

                elif brand == 'today':
                    self.log_update.emit("오늘의집")
                    #옵션 - 셀레니움
                    options = webdriver.ChromeOptions()
                    options.add_argument("--disable-blink_features=AutomationControlled")
                    options.add_experimental_option("excludeSwitches",["enable_logging"])
                    options.add_argument("no_sandbox")
                    options.add_argument("--start-maximized")
                    options.add_argument("disable-infobars")
                    options.add_argument("--disable-extionsions")
                    options.add_experimental_option("useAutomationExtension",False)
                    options.add_argument("headless")
                    options.add_argument("disable-gpu")
                    options.add_argument("lang=ko_KR")
                    driver = webdriver.Chrome(options=options)
                    actions = ActionChains(driver)
                    url = 'https://ohou.se/brands/home?query=%EC%9E%A5%EC%9D%B8%EA%B0%80%EA%B5%AC'

                    driver.get(url)
                    time.sleep(.5) # 1

                    scroll_height = 10000

                    while True:
                            
                        html = driver.page_source
                        soup = bs(html, 'html.parser')

                        elems = soup.find_all('a', 'production-item__overlay')

                        o_cnt = 1
                        for el in range(len(elems)):
                            # 상세페이지 url
                            o_url = 'https://ohou.se' + elems[el]['href']

                            # save sql db
                            sql_statements = [f"insert into bbang_ttol (url) values ('{o_url}');"]
                            sql_proc(sql_statements)

                            # log
                            self.log_update2.emit(f"상세페이지 총 {o_cnt}개 수집")
                            print(f'오늘의집 {o_cnt}')
                            o_cnt += 1


                        # o_lists = list(dict.fromkeys(o_lists))
                        test = int((ratio/400)*o_cnt+ratio*3)
                        self.progress_update.emit(test)

                        # Scroll down by the defined amount
                        driver.execute_script(f"window.scrollBy(0, {scroll_height});")
                        time.sleep(.5)

                        # get the current scroll position
                        scroll_position = driver.execute_script("return window.pageYOffset;")


                        # 마지막 페이지 확인
                        if 'temp_scroll_postion' in locals() and temp_scroll_postion == scroll_position:
                            break

                        # 아니면 계속 리스트 수집
                        temp_scroll_postion = scroll_position
                    
                    # log
                    self.log_update2.emit(f"{date} 상세페이지 파일 업로드")
                    print(f'{date} 상세페이지 파일 업로드')

                elif brand == 'sin':
                    self.log_update.emit("신세계")
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
                    page = 1

                    sin_cnt = 1
                    while True:
                        url = f'https://www.ssg.com/search.ssg?target=all&query=%EC%9E%A5%EC%9D%B8%EA%B0%80%EA%B5%AC%2B%EB%8F%99%EC%84%9C%EA%B0%80%EA%B5%AC&brand=2000020584&count=100&page={page}'
                        res = requests.get(url, headers=headers, verify=False)
                        print(f'신세계 {page}page')

                        ck_end = res.text.count('검색어와 일치하는 상품이 없습니다.')
                        if ck_end == 1: # page가 넘어갔을 경우break
                            print('신세계 수집종료')
                            self.log_update2.emit(f"{date} 상세페이지 파일 업로드")
                            break
                        else:
                            soup = bs(res.text, 'html.parser')
                            time.sleep(.5)
                            elem = soup.find("ul", id="idProductImg")
                            elems = elem.find_all("li")

                            for el in range(len(elems)):

                                # log
                                test = int((ratio/len(elems))*el+ratio*4)
                                self.progress_update.emit(test)

                                # 상세페이지 url
                                sin_url = elems[el]['id'].replace('item_unit_','https://www.ssg.com/item/itemView.ssg?itemId=')

                                # save sql db
                                sql_statements = [f"insert into bbang_ttol (url) values ('{sin_url}');"]
                                sql_proc(sql_statements)

                                # log
                                self.log_update2.emit(f"상세페이지 총 {sin_cnt}개 수집")   
                                print(url)
                                sin_cnt += 1
                            
                            # log
                            print(f'신세계 {sin_cnt}')
                            page += 1

                elif brand == 'gmarket':
                    self.log_update.emit("지마켓")
                    url = 'https://browse.gmarket.co.kr/search?keyword=장인가구+동서가구'
                    response = requests.get(url)
                    soup = bs(response.text, 'html.parser')
                    a_tags = soup.find_all('a', 'link__shop')

                    url2 = 'http://item.gmarket.co.kr/Item?goodscode='
                    
                    gm_cnt = 1
                    for tag in range(len(a_tags)):

                        # log
                        test = int((ratio/len(a_tags))*tag+ratio*5)
                        self.progress_update.emit(test)

                        # 상세페이지 url
                        gm_url = url2 + str(a_tags[tag].get('data-montelena-goodscode')).strip('[]"\'')

                        # save sql db
                        sql_statements = [f"insert into bbang_ttol (url) values ('{gm_url}');"]
                        sql_proc(sql_statements)

                        # log
                        self.log_update2.emit(f"상세페이지 총 {gm_cnt}개 수집")   
                        print(f'지마켓 {gm_cnt}')

                    # log                    
                    self.log_update2.emit(f"{date} 상세페이지 파일 업로드")
                    
                    
                elif brand == 'auction':
                    self.log_update.emit("옥션")
                    auc_lists = []
                    for pg in range(1,6):
                        test = int((ratio/5)*pg+ratio*6)
                        self.progress_update.emit(test)
                        url = f'https://browse.auction.co.kr/search?keyword=%ec%9e%a5%ec%9d%b8%ea%b0%80%ea%b5%ac%2b%eb%8f%99%ec%84%9c%ea%b0%80%ea%b5%ac&itemno=&nickname=&encKeyword=%25EC%259E%25A5%25EC%259D%25B8%25EA%25B0%2580%25EA%25B5%25AC%252B%25EB%258F%2599%25EC%2584%259C%25EA%25B0%2580%25EA%25B5%25AC&arraycategory=&frm=&dom=auction&isSuggestion=No&retry=&k=0&p={pg}'
                        response = requests.get(url)

                        html_content = response.text
                        soup = bs(html_content, 'html.parser')
                        a_tags = soup.find_all('a')

                        hrefs = [a_tag['href'] for a_tag in a_tags if 'href' in a_tag.attrs if 'itempage3' in a_tag['href']]
                        hrefs = hrefs[::2]

                        auc_cnt = 1
                        for href in hrefs:

                            # save sql db
                            sql_statements = [f"insert into bbang_ttol (url) values ('{href}');"]
                            sql_proc(sql_statements)
                            
                            # log
                            self.log_update2.emit(f"상품페이지 총 {auc_cnt}개 수집")
                            print(f'옥션 {auc_cnt}')
                            auc_cnt += 1

                    # log
                    self.log_update2.emit(f"{date} 상세페이지 파일 업로드")

                elif brand == 'interpark':
                    self.log_update.emit("인터파크")
                    interpark_cnt = 1
                    for i in range(134): 
                        try:
                            url = f'https://shopping.interpark.com/niSearch/shop/listPrdChoiceAndNormal.json?pis1=shop&page={i+1}&keyword=바스포르&rows=52'
                            res = requests.get(url)
                            data = json.loads(res.text)
                            test = int((ratio/134)*i+ratio*7)
                            self.progress_update.emit(test)
                            cnt = len(data['data']['listChoiceAndNormal'][0])
                            for j in range(cnt+1):
                                try:
                                    # 상세페이지 url
                                    item_url = 'https://shopping.interpark.com/product/productInfo.do?prdNo=' + str(data['data']['listChoiceAndNormal'][j]['prdNo'])

                                    # save sql db
                                    sql_statements = [f"insert into bbang_ttol (url) values ('{item_url}');"]
                                    sql_proc(sql_statements)

                                    # log
                                    self.log_update2.emit(f"상세페이지 총 {interpark_cnt}개 수집")
                                    print(f'인터파크 {interpark_cnt}')
                                    interpark_cnt += 1
                                except:
                                    pass
                        except:
                            pass
                    
                    # log
                    self.log_update2.emit(f"{date} 상세페이지 파일 업로드")
                    
                elif brand == 'coupang':
                    self.log_update.emit("쿠팡")
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
                    
                    driver.get("https://store.coupang.com/vp/vendors/A00037308/products")
                    time.sleep(.5)

                    page_height = driver.execute_script("return document.body.scrollHeight")
                    scroll_height = page_height // 2.5
                    driver.execute_script("window.scrollTo(0, {});".format(scroll_height))
                    ul_elements = driver.find_elements(By.CLASS_NAME,'scp-component-filter-options__option-items__btn-fold')

                    # log
                    self.log_update.emit('open category')
                    cnt = 0
                    for ul_element in ul_elements:
                        driver.execute_script("arguments[0].click();", ul_element) # 버튼 클릭
                        print(ul_element.text)
                        time.sleep(.5)
                        cnt += 1
                        print(cnt)
                    print(f'final {cnt}')
                    html = driver.page_source
                    soup = bs(html,'html.parser')


                    label_tags = soup.find_all('label')
                    cnt = 0
                    tag_list = []
                    for tag in label_tags:
                        if str(tag).__contains__('for="component'):
                            parent = tag.parent
                            if not str(parent).__contains__('href'):
                                cnt += 1
                                tag = str(tag).split(sep='=')[1].split(sep='t')[1].split(sep='"')[0]
                                tag_list.append(tag)

                    tag_list = tag_list[1:] # 0: empty tag


                    def process_urls(tag_list,list_start,list_end):
                        print(list_start, list_end)
                        detail_url = []
                        for i in range(list_start, list_end):
                            # log
                            test = int((ratio/len(tag_list)*i+ratio*8))
                            self.progress_update.emit(test)
                            print(i, '/', list_end)
                            tag = tag_list[i]

                            driver = webdriver.Chrome(options=options)
                            url = f'https://store.coupang.com/vp/vendors/A00037308/product/lists?componentId={tag}&pageNum=1'
                            driver.get(url)
                            elem = driver.find_element(By.TAG_NAME, 'body').text

                            find_word = '"itemTotalCount":'
                            total_cnt = elem[elem.find(find_word) + len(find_word):]
                            total_cnt = int(total_cnt[:total_cnt.find(",")])

                            cnt = math.ceil(int(total_cnt)/30)

                            #if total cnt = 0?


                            file_path = 'cou_list.csv'
                            for pageNum in range(1, cnt+1):
                                url = f'https://store.coupang.com/vp/vendors/A00037308/product/lists?componentId={tag}&pageNum={str(pageNum)}'
                                driver.get(url)
                                find_word = 'link'
                                elem = driver.find_element(By.TAG_NAME, 'body').text
                                cnt = elem.count(find_word)
                                for i in range(cnt):
                                    search2 = elem[elem.find(find_word) + len(find_word)+3:]
                                    elem = search2
                                    search2 = search2[:search2.find('"')]

                                    detail_url.append(search2)
                                    self.log_update2.emit(f"상세페이지 총 {len(detail_url)}개 수집")
                                    print(f'쿠팡 {len(detail_url)}')
                                print(url)
                                time.sleep(1)
                            detail_url = list(set(detail_url)) # 중복제거

                            
                            with open(file_path, "a", newline='',encoding="utf-8") as f:
                                writer = csv.writer(f)
                                for url in detail_url:
                                    writer.writerow([url])
                            self.log_update2.emit(f"{date} 상세페이지 파일 업로드")
                            time.sleep(5)
                            driver.close()
                        return detail_url

                    detail_url = process_urls(tag_list,1,165) # 근데 왜 1, 165일까...............

                    for cou_url in detail_url:
                        sql_statements = [f"insert into bbang_ttol (url) values ('{cou_url}');"]
                        sql_proc(sql_statements)
                        print(f'{detail_url.index(cou_url)}/{len(detail_url)}')
                        # print('herehereherehereherehereherehereherehereherehereherehere')

                            # print(total_cnt)

                            # cnt = math.ceil(int(total_cnt)/30)



                    # total = len(tag_list)
                    # num_intervals = 1 # thread 개수
                    # interval_size = total // num_intervals

                    # for i in range(num_intervals):
                    #     start = i * interval_size + 1
                    #     end = (i + 1) * interval_size


                    #     if i == num_intervals - 1:
                    #         end += total % num_intervals

                    #     threads = []
                    #     # print(start,'/',end)
                    #     # print(num_threads)
                    #     thread = threading.Thread(target=process_urls, args=(tag_list, start ,end))
                    #     thread.start()
                    #     threads.append(thread)

                self.progress_update.emit(cnt*ratio)
                cnt += 1 

        date,check = get_week()
        if check == '다운로드 필요':
            get_list(date)
            print('모든 브랜드 상세페이지 파일 업로드')
            # log
            self.log_update2.emit("모든 브랜드 상세페이지 파일 업로드")



                

    def stop(self):
        self.log_update2.emit("다운로드 완료")
        # Stop the thread gracefully
        pass

class PopupDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Item list check & Download")
        self.resize(400, 1)

        layout = QVBoxLayout(self)
        self.progress_bar = QProgressBar(self)
        label_log = QLabel('log')
        label_log2 = QLabel('log2')

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.progress_bar)
        vbox1.addWidget(label_log)
        vbox1.addWidget(label_log2)

        layout.addLayout(vbox1)

        # Create a worker thread to perform the independent work
        self.worker_thread = WorkerThread_list_get()
        self.worker_thread.progress_update.connect(self.update_progress)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_update2.connect(label_log2.setText)
        self.worker_thread.finished.connect(self.close_dialog)
        self.finished.connect(self.worker_thread.stop)
        self.showEvent = self.start_work

    def start_work(self, event):
        self.worker_thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def close_dialog(self):
        self.close()
        

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.thread_running = False

        def closeEvent(self, event):
            reply = QMessageBox.question(self, 'Confirm Close', 'Are you sure you want to exit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                #크롬, 크롬드라이버 프로세서 종료
                processes = [p for p in psutil.process_iter(['pid', 'name', 'create_time'])]
                processes_sorted = sorted(processes, key=lambda x: x.info['create_time'], reverse=True)

                #프로세스 내 chromedriver.exe가 있으면 chrome, chromedriver 종료
                for process in processes_sorted:
                    print(f"PID: {process.info['pid']} Name: {process.info['name']} Created: {process.create_time()}")
                    if process.info['name'] == 'chromedriver.exe':

                        for process in processes_sorted:
                            print(f"PID: {process.info['pid']} Name: {process.info['name']} Created: {process.create_time()}")

                            if process.info['name'] == 'chrome.exe':
                                process_id = process.info['pid']
                                process = psutil.Process(process_id)
                                process.terminate()
                            elif process.info['name'] == 'chromedriver.exe':
                                process_id = process.info['pid']
                                process = psutil.Process(process_id)
                                process.terminate()
                                break
                        event.accept()
                event.accept()
            else:
                event.ignore()

    def initUI(self):
        self.login_id = getpass.getuser()

        리스트받아오기 = QAction('리스트받아오기', self)
        쿠팡 = QAction('쿠팡', self)
        ll번가 = QAction('11번가', self)
        롯데온 = QAction('롯데온', self)
        스마트스토어 = QAction('스마트스토어', self)
        신세계 = QAction('신세계', self)
        오늘의집 = QAction('오늘의집', self)
        인터파크 = QAction('인터파크', self)
        옥션 = QAction('옥션', self)
        지마켓 = QAction('지마켓', self)

        self.statusBar()

        self.toolbar = QToolBar()
        self.toolbar.addAction(리스트받아오기)
        self.toolbar.addAction(쿠팡)
        self.toolbar.addAction(ll번가)
        self.toolbar.addAction(롯데온)
        self.toolbar.addAction(스마트스토어)
        self.toolbar.addAction(신세계)
        self.toolbar.addAction(오늘의집)
        self.toolbar.addAction(인터파크)
        self.toolbar.addAction(옥션)
        self.toolbar.addAction(지마켓)

        self.addToolBar(self.toolbar)

        # toolbar action
        리스트받아오기.triggered.connect(self.open_popup)
        쿠팡.triggered.connect(self.cou)
        ll번가.triggered.connect(self.llst)
        롯데온.triggered.connect(self.lot)
        스마트스토어.triggered.connect(self.ss)
        신세계.triggered.connect(self.sin)
        오늘의집.triggered.connect(self.oj)
        인터파크.triggered.connect(self.interpark)
        옥션.triggered.connect(self.auction)
        지마켓.triggered.connect(self.gmarket)

        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 800, 600)
        self.show()

    # 쿠팡함수
    def cou(self):

        if self.thread_running:
            # Don't run the thread if it's already running
            return

        self.toolbar.setEnabled(False)

        label_1 = QLabel('쿠팡 수집')
        label_log = QLabel('쿠팡 수집')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap(f"test1_{self.login_id}.jpg")
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        # desired_height = int(available_width / aspect_ratio)
        desired_height = 300

        # set the maximum size of the label_img widget to fit the available width and maintain the aspect ratio
        label_img.setMaximumSize(available_width, desired_height)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(progressBar)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(textEdit, 7)
        vbox1.addWidget(textEdit2, 3)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1, 5)
        hbox2.addWidget(label_img, 5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(label_log)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create and start the worker thread
        test = '쿠팡'
        self.worker_thread = WorkerThread_mall(test)
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def llst(self):

        if self.thread_running:
            # Don't run the thread if it's already running
            return

        self.toolbar.setEnabled(False)

        label_1 = QLabel('11번가 수집')
        label_log = QLabel('log')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap(f"test1_{self.login_id}.jpg")
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        # desired_height = int(available_width / aspect_ratio)
        desired_height = 300

        # set the maximum size of the label_img widget to fit the available width and maintain the aspect ratio
        label_img.setMaximumSize(available_width, desired_height)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(progressBar)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(textEdit, 7)
        vbox1.addWidget(textEdit2, 3)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1, 5)
        hbox2.addWidget(label_img, 5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(label_log)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create and start the worker thread
        test = 'llst'
        self.worker_thread = WorkerThread_mall(test)
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def lot(self):


        if self.thread_running:
            # Don't run the thread if it's already running
            return

        self.toolbar.setEnabled(False)

        label_1 = QLabel('롯데온 수집')
        label_log = QLabel('log')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap(f"test1_{self.login_id}.jpg")
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        # desired_height = int(available_width / aspect_ratio)
        desired_height = 300

        # set the maximum size of the label_img widget to fit the available width and maintain the aspect ratio
        label_img.setMaximumSize(available_width, desired_height)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(progressBar)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(textEdit, 7)
        vbox1.addWidget(textEdit2, 3)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1, 5)
        hbox2.addWidget(label_img, 5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(label_log)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create and start the worker thread
        test = 'lot'
        self.worker_thread = WorkerThread_mall(test)
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def ss(self):
        

        if self.thread_running:
            # Don't run the thread if it's already running
            return

        self.toolbar.setEnabled(False)

        label_1 = QLabel('네이버스마트스토어 수집')
        label_log = QLabel('log')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap(f"test1_{self.login_id}.jpg")
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        # desired_height = int(available_width / aspect_ratio)
        desired_height = 300

        # set the maximum size of the label_img widget to fit the available width and maintain the aspect ratio
        label_img.setMaximumSize(available_width, desired_height)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(progressBar)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(textEdit, 7)
        vbox1.addWidget(textEdit2, 3)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1, 5)
        hbox2.addWidget(label_img, 5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(label_log)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create and start the worker thread
        test = 'ss'
        self.worker_thread = WorkerThread_mall(test)
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def sin(self):


        if self.thread_running:
            # Don't run the thread if it's already running
            return

        self.toolbar.setEnabled(False)

        label_1 = QLabel('신세계 수집')
        label_log = QLabel('log')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap(f"test1_{self.login_id}.jpg")
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        # desired_height = int(available_width / aspect_ratio)
        desired_height = 300

        # set the maximum size of the label_img widget to fit the available width and maintain the aspect ratio
        label_img.setMaximumSize(available_width, desired_height)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(progressBar)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(textEdit, 7)
        vbox1.addWidget(textEdit2, 3)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1, 5)
        hbox2.addWidget(label_img, 5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(label_log)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create and start the worker thread
        test = 'sin'
        self.worker_thread = WorkerThread_mall(test)
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def oj(self):


        if self.thread_running:
            # Don't run the thread if it's already running
            return

        self.toolbar.setEnabled(False)

        label_1 = QLabel('오늘의집 수집')
        label_log = QLabel('log')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap(f"test1_{self.login_id}.jpg")
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        # desired_height = int(available_width / aspect_ratio)
        desired_height = 300

        # set the maximum size of the label_img widget to fit the available width and maintain the aspect ratio
        label_img.setMaximumSize(available_width, desired_height)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(progressBar)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(textEdit, 7)
        vbox1.addWidget(textEdit2, 3)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1, 5)
        hbox2.addWidget(label_img, 5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(label_log)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create and start the worker thread
        test = 'oj'
        self.worker_thread = WorkerThread_mall(test)
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def interpark(self):


        if self.thread_running:
            # Don't run the thread if it's already running
            return

        self.toolbar.setEnabled(False)

        label_1 = QLabel('인터파크 수집')
        label_log = QLabel('log')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap(f"test1_{self.login_id}.jpg")
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        # desired_height = int(available_width / aspect_ratio)
        desired_height = 300

        # set the maximum size of the label_img widget to fit the available width and maintain the aspect ratio
        label_img.setMaximumSize(available_width, desired_height)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(progressBar)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(textEdit, 7)
        vbox1.addWidget(textEdit2, 3)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1, 5)
        hbox2.addWidget(label_img, 5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(label_log)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create and start the worker thread
        test = 'interpark'
        self.worker_thread = WorkerThread_mall(test)
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def auction(self):


        if self.thread_running:
            # Don't run the thread if it's already running
            return

        self.toolbar.setEnabled(False)

        label_1 = QLabel('옥션 수집')
        label_log = QLabel('log')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap(f"test1_{self.login_id}.jpg")
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        # desired_height = int(available_width / aspect_ratio)
        desired_height = 300

        # set the maximum size of the label_img widget to fit the available width and maintain the aspect ratio
        label_img.setMaximumSize(available_width, desired_height)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(progressBar)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(textEdit, 7)
        vbox1.addWidget(textEdit2, 3)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1, 5)
        hbox2.addWidget(label_img, 5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(label_log)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create and start the worker thread
        test = 'auction'
        self.worker_thread = WorkerThread_mall(test)
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def gmarket(self):


        if self.thread_running:
            # Don't run the thread if it's already running
            return

        self.toolbar.setEnabled(False)

        label_1 = QLabel('지마켓 수집')
        label_log = QLabel('log')
        progressBar = QProgressBar()
        progressBar.setValue(0)
        textEdit = QTextEdit()
        textEdit2 = QTextEdit()

        # create the label widget and set its pixmap
        label_img = QLabel()
        pixmap = QPixmap(f"test1_{self.login_id}.jpg")
        label_img.setPixmap(pixmap)

        # calculate the desired size based on the available width and the image's aspect ratio
        available_width = 400
        # desired_height = int(available_width / aspect_ratio)
        desired_height = 300

        # set the maximum size of the label_img widget to fit the available width and maintain the aspect ratio
        label_img.setMaximumSize(available_width, desired_height)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label_1)
        hbox1.addWidget(progressBar)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(textEdit, 7)
        vbox1.addWidget(textEdit2, 3)

        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1, 5)
        hbox2.addWidget(label_img, 5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(label_log)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Create and start the worker thread
        test = 'gmarket'
        self.worker_thread = WorkerThread_mall(test)
        self.worker_thread.log_update.connect(textEdit.append)
        self.worker_thread.log_update.connect(label_log.setText)
        self.worker_thread.log_img_update.connect(textEdit2.append)
        self.worker_thread.progress_update.connect(progressBar.setValue)
        self.worker_thread.pixmap_update.connect(label_img.setPixmap)
        # delete the thread when finished
        self.worker_thread.finished.connect(self.worker_thread.deleteLater)
        self.worker_thread.finished.connect(self.resetThreadRunning)  # reset the flag when finished

        self.thread_running = True
        self.worker_thread.start()

    def resetThreadRunning(self):
        self.thread_running = False

    def open_popup(self):
        popup = PopupDialog(self)
        popup.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())