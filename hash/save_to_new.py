# 몰 개수 = DB index 개수
# Ex) 0,1,2,3,….,9

# 2. Hash function = askii 코드를 DB index 개수로 나눈 나머지 
# Ex)
# Specific_index = hash_fun(mall_name)
# Return 3 

# 3. Firebase 연결 
# If ) Specific_index name == folder name : save file
# Else) Specific_index name != folder name : make file name(기존 + len(폴더개수)) then save file


