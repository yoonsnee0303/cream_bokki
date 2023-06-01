# 스크롤
# 폴더명 지정
from ascii_code import make_dicts
import pyautogui


import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage



def save_file(brand_lists,brand_dicts,file_name):
    pyautogui.screenshot(f'{file_name}.jpg')
    image_file_path = f'{file_name}.jpg'
    for brand in brand_lists:
        if brand in file_name:

            #make bucket and get folder name for each brand
            bucket = storage.bucket()
            folder_name = str(list(brand_dicts[brand].keys())[0])
            folder_blob = bucket.blob(folder_name)

            #check specific folder name exist or not
            if not folder_blob.exists():
                print(f'Creating folder {folder_name}')
                folder_blob.upload_from_string('')

            # Upload a file to the folder
            blob = bucket.blob(f'{folder_name}/{image_file_path}')
            blob.upload_from_filename(image_file_path)
            print(f'File {file_name} uploaded to {folder_name}')