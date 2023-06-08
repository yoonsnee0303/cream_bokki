import os
import firebase_admin
from firebase_admin import credentials, initialize_app
from firebase_admin import storage as firebase_storage
from google.cloud import storage

# Firebase 인증 정보 설정
cred = credentials.Certificate('upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json')

# Firebase 프로젝트 ID
project_id = 'upload-img-5b02f'

# Firebase 초기화
firebase_admin.initialize_app(cred, {'storageBucket': f'{project_id}.appspot.com'})

# Firebase Storage 인스턴스 생성
bucket = firebase_storage.bucket()

# 모든 폴더 내 파일 다운로드 함수
def download_files_from_folder(folder_path):
    # 폴더 내 파일 목록 가져오기
    blobs = bucket.list_blobs(prefix=folder_path)

    for blob in blobs:
        # 파일이 폴더인 경우 재귀적으로 호출하여 폴더 내 파일 다운로드
        if blob.name.endswith('/'):
            sub_folder_path = os.path.join(folder_path, os.path.basename(blob.name))
            download_files_from_folder(sub_folder_path)
        else:
            # 파일 다운로드
            file_path = blob.name
            file_name = os.path.basename(file_path)
            blob.download_to_filename(file_name)

# Firebase Storage의 모든 폴더 내 파일 다운로드
download_files_from_folder("")

print("다운로드가 완료되었습니다.")
