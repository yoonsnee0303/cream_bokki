


from google.cloud import storage
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage as firebase_storage
import os

# Firebase 인증 정보 설정
cred = credentials.Certificate('upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json')

# Firebase 프로젝트 ID
project_id = 'upload-img-5b02f'

# Firebase 초기화
firebase_admin.initialize_app(cred, {'storageBucket': f'{project_id}.appspot.com'})

# Firebase Storage 인스턴스 생성
bucket = firebase_storage.bucket()

# 새 폴더 이름을 설정합니다.
new_folder_name = '5월2주차'

# Firebase Storage에 새 폴더를 생성합니다.
new_folder = bucket.blob(new_folder_name + '/')

# 모든 파일을 가져오고 다운로드하여 새 폴더에 저장합니다.
blobs = bucket.list_blobs()
for blob in blobs:
    # 다운로드할 파일의 경로 및 이름을 설정합니다.
    destination_file = os.path.join('upload-img-5b02f.appspot.com/', blob.name)

    # 파일을 다운로드합니다.
    blob.download_to_filename(destination_file)
    print(f"다운로드 완료: {destination_file}")

    # 새 폴더에 파일을 업로드합니다.
    new_file_path = new_folder_name + '/' + blob.name
    new_blob = bucket.blob(new_file_path)
    new_blob.upload_from_filename(destination_file)
    print(f"업로드 완료: {new_file_path}")

    # 다운로드한 파일을 삭제합니다.
    os.remove(destination_file)
    print(f"파일 삭제: {destination_file}")

print("파일 다운로드, 업로드, 및 삭제가 완료되었습니다.")



