# 파일 이름 받아오기
# 파일 이름 아스키 코드로 변환
# 
dicts = {
    0:[],
    1:[]
}

# 몰 개수 = DB index 개수
# Ex) 0,1,2,3,….,9

# 2. Hash function = askii 코드를 DB index 개수로 나눈 나머지 
# Ex)
# Specific_index = hash_fun(mall_name)
# Return 3 

# 3. Firebase 연결 
# If ) Specific_index name == folder name : save file
# Else) Specific_index name != folder name : make file then save file

# 현재 db에 저장되어있는 파일 이름의 hash function return 값 (specific index) 파악
# Ex) 쿠팡: 0, 신세계, 1

# 2. 각 index 개수별로 dict (key:int – value:list) 만들기
# Ex) 
# {0:[], 1:[]}

# 3. Firebase로 파일 읽기 then index값 구별하기
# Ex)
# If basfor.count > 0 : index = 0, 
# Else: index = 1,

# 4. Index별 dict key matching하여 list value에 append

# 5. 폴더 만들어 list data, firebase에 upload.

