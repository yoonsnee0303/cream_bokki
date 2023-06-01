import pytesseract
import cv2
from matplotlib import pyplot as plt
import urllib.request

import time
import os
import urllib3
from PIL import Image
import sys
import unittest

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

                    if img_width != 492:
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

                    if now_hight > 30:
                        return '이미지없음'
                    elif text.count('동서가구') + text.count('동셔가구') + text.count('써가구') + text.count('도서가구') != 0:
                        #plt.show()
                        return '동서가구'
            except:
                pass


        image, img_width, img_hight, width_unit, hight_unit = 이미지확인(url)
        check = 상단글자(image, width_unit, hight_unit, img_width, img_hight)
        print(check)

        return check

url = 'https://thumbnail10.coupangcdn.com/thumbnails/remote/q89/image/retail/images/2022/02/09/18/4/414822b8-0beb-4330-b390-439249971fc6.jpg'
img_check(url)