import os
from firebase_admin import credentials, initialize_app
from google.cloud import storage

# Firebase Admin SDK 인증 정보
cred = credentials.Certificate("upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json")
initialize_app(cred)

# 옮길 폴더 경로와 새로운 폴더 경로
current_folder_path = "folder1"
new_folder_path = "folder2"

# Google Cloud Storage 클라이언트 초기화
client = storage.Client()

# 폴더 내 파일 목록 가져오기
bucket = client.get_bucket("your-bucket-name")
blobs = bucket.list_blobs(prefix=current_folder_path)

# 각 파일을 새로운 경로로 옮기고 업로드하기
for blob in blobs:
    old_blob_path = blob.name
    new_blob_path = old_blob_path.replace(current_folder_path, new_folder_path)

    # 새로운 경로로 파일 복사
    new_blob = bucket.copy_blob(blob, bucket, new_blob_path)

    # 이전 경로의 파일 삭제 (선택 사항)
    blob.delete()

    print(f"Moved {old_blob_path} to {new_blob_path}")