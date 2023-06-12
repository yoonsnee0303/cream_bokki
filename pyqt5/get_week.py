
from google.cloud import storage
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage as firebase_storage
import os
import datetime
import numpy as np


def get_week_of_month(date):
    first_day = date.replace(day=1)
    adjusted_day = first_day + datetime.timedelta(days=(6 - first_day.weekday()))
    week_number = (date - adjusted_day).days // 7 + 2
    return week_number


# Firebase 인증 정보 설정
cred = credentials.Certificate('upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json')

# Firebase 프로젝트 ID
project_id = 'upload-img-5b02f'

# Firebase 초기화
firebase_admin.initialize_app(cred, {'storageBucket': f'{project_id}.appspot.com'})

# Firebase Storage 인스턴스 생성
bucket = firebase_storage.bucket()

blobs = bucket.list_blobs()


# 현재 날짜 구하기
current_date = datetime.date.today()

# 현재 월의 주차와 월 출력
week_of_month = get_week_of_month(current_date)
month = current_date.strftime("%m월")
date = month[1:3] + str(week_of_month) + '주차'
for l in list(range(10,12)): # 10월 11월 12월
    if str(l) in month:
        date = month[:3] + str(week_of_month) + '주차'
        print(date)
for blob in blobs:
    # print(blob.name)
    folder_name = blob.name.split('/')[0]
    if date == folder_name:
        print(f'{date}는 이미 다운로드 되어있는 주차입니다.')
        break
    else:

