from PyQt5.QtWidgets import QFileDialog, QApplication
import firebase_admin
from firebase_admin import credentials, storage


import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

import os

import tempfile


# 전체 폴더명 가지고 오기
cred = credentials.Certificate('upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json')

project_id = 'upload-img-5b02f.appspot.com'

firebase_admin.initialize_app(cred)

bucket = storage.bucket(project_id)
print(bucket)
# 업로드할 파일 경로
file_path = './today_20230502_182019_628244_img.jpg'
print('ck1')
# 저장할 파일명 (Firebase에 업로드될 파일명)
destination_blob_name = '5월2주차/today/today_20230502_182019_628244_img.jpg'

# 파일 업로드
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(file_path)

print('파일이 업로드되었습니다.')