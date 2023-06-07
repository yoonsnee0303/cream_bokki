import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage # Firebase 라이브러리를 사용하는 방식에 따라 import 방법이 달라질 수 있습니다.
import datetime
import os


def move_folder(source, destination):
    try:
        os.rename(source, destination)
        print("폴더 이동이 완료되었습니다.")
    except FileNotFoundError:
        print("폴더를 찾을 수 없습니다.")
    except FileExistsError:
        print("대상 폴더가 이미 존재합니다.")

def create_folder_with_month_and_week(path):
    today = datetime.date.today()
    month = today.month
    week_number = (today.day - 1) // 7 + 1
    folder_name = f"{month}월 {week_number}주차"
    folder_path = os.path.join(path, folder_name)
    os.makedirs(folder_path)
    print(f"폴더가 생성되었습니다: {folder_path}")






# 전체 폴더명 가지고 오기
cred = credentials.Certificate('upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json')

project_id = 'upload-img-5b02f.appspot.com'

firebase_admin.initialize_app(cred)

bucket = storage.bucket(project_id)

blobs = bucket.list_blobs() #prefix=folder_name

folder_names = set()

for blob in blobs:
    folder_names.add(blob.name.split('/')[0])
folder_names = list(folder_names)


import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

def move_folder(source_folder, destination_folder):
    # Firebase Storage 버킷 참조
    bucket = storage.bucket()

    # 원본 폴더 내의 파일 목록 가져오기
    source_files = bucket.list_blobs(prefix=source_folder)

    for file in source_files:
        # 파일 경로에서 원본 폴더명 제거
        destination_path = file.name.replace(source_folder, destination_folder, 1)

        # 새로운 위치에 파일 복사
        new_blob = bucket.blob(destination_path)
        new_blob.upload_from_string(file.download_as_bytes())

        # # 원본 폴더 내 파일 삭제
        # file.delete()

    print('폴더 이동이 완료되었습니다.')

# 사용 예시
move_folder('폴더1/', '5월 2주차야/')


    # 원래 폴더 삭제 (선택 사항)
    # original_folder = bucket.blob(folder_name + "/")
    # original_folder.delete()


# for folder_name in folder_names:
#     folder_name = '135/'
#     blobs = bucket.list_blobs(prefix=f'{folder_name}') 
    
#     file_list = []
#     for file in blobs:
#         file_list.append(file)
#     print(file_list)

# # Firebase에서 폴더명 가져오기
# firebase = firebase.FirebaseApplication('https://your-firebase-database.firebaseio.com/', None)  # Firebase 프로젝트 URL로 변경해야 합니다.
# result = firebase.get('/folders', None)  # Firebase의 'folders' 경로에 폴더들이 저장되어 있다고 가정합니다.

# # 폴더 이동을 수행할 경로 지정
# destination_path = "이동할 경로/"

# # 대상 폴더 경로 생성
# destination_path = os.path.join(destination_path, folder_name)