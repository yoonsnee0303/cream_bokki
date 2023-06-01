# 현재 db에 저장 되어 있는 파일 이름의 hash function return 값 (specific index) 파악
# Ex) 쿠팡: 0, 신세계, 1

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import db

# Firebase certificate
cred = credentials.Certificate('upload-img-5b02f-firebase-adminsdk-frojl-fe3e21064f.json')

# Firebase project id
project_id = 'upload-img-5b02f.appspot.com'

# Firebase initializing
firebase_admin.initialize_app(cred, {'storageBucket': f'{project_id}'})

brand_lists = ['coupang','sin']

# changes into the ascii code
def toAscii(str1,brand_lists):
    ascii_str = int(sum([ord(spell) for spell in str1]) / len(brand_lists))
    return ascii_str

# make dicts
brand_dicts = {}
for brand in brand_lists:
    to = toAscii(brand,brand_lists)
    brand_dicts[to] = []
    # print(brand,brand_dicts)

# setting brand_key
coupang_key = [k for k in brand_dicts.keys()][0]
sin_key = [k for k in brand_dicts.keys()][1]

# firebase
# firebase
# firebase

# firebase file lists
blobs = storage.bucket().list_blobs()
file_names = [blob.name for blob in blobs]

cnt = 0
for name in file_names:

    # checking number in file's name
    isnum = name.split('_')[0].isdigit()

    # move orgin file in new folder
    bucket = storage.bucket()

    # setting the file_name 
    ori_file_path = name

    # coupang 165
    if isnum == True:

        brand_dicts[165].append(name)

        # 이동할 파일의 blob 객체 생성
        blob = bucket.blob(ori_file_path) 

        # 새로운 경로와 이름으로 blob 객체 복사
        new_file_path = f'{coupang_key}/{name}' 
        new_blob = bucket.copy_blob(blob, bucket, new_file_path)

        # 이전 경로에 있는 blob 객체 삭제
        # blob.delete()
        print(new_file_path)
        cnt += 1

    
    # sinsagae 374
    else:

        brand_dicts[374].append(name)

        # 이동할 파일의 blob 객체 생성
        blob = bucket.blob(ori_file_path)

        # 새로운 경로와 이름으로 blob 객체 복사
        new_file_path = f'{sin_key}/{name}' 
        new_blob = bucket.copy_blob(blob, bucket, new_file_path)

        # 이전 경로에 있는 blob 객체 삭제
        # blob.delete()
        print(new_file_path)
        cnt += 1
    print(f'{cnt}/{file_names}')


# print(brand_dicts)
