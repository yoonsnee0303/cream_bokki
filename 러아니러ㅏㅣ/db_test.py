import pymysql
import csv
import random

# execute query
def execute_query(query1):
    # Connect to the database
    connection = pymysql.connect(
        host='121.254.162.132',
        user='capture',
        password='edf@@0907',
        database='edf_capture'
    )



    # Create a cursor object
    cursor = connection.cursor()

    # Execute the SQL query
    cursor.execute(query1)

    if 'select' in query1: 
        rows = cursor.fetchall()
        
        for row in rows:
            print(row)

        print("Query executed successfully!")
    
    else:
        connection.commit()

        rows = cursor.fetchall()
        for row in rows:
            print(row)
        
        print("Query executed successfully!")
        


# excel 파일 불러오기
def read_csv_as_list(file_path):
    data = []
    
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    
    return data[0]


# db 생성
brand_lists = ['coupang','ssg','11st','auction','ohou','naver','gmarket','lotteimall','interpark']
table_name = 'test1'
csv_file_path = 'all_lists.csv'
csv_data = read_csv_as_list(csv_file_path)
cnt = 1
for data in csv_data:
    # # brand
    # for brand in brand_lists:
    #     # if 'coupang' in brand:
    #     #     value = brand
    #     # elif 'ssg' in brand:
    #     #     value = brand
    #     # elif '11st' in brand:
    #     #     value = brand
    #     # elif 'auction' in brand:
    #     #     value = brand
    #     # elif 'ohou' in brand:
    #     #     value = brand
    #     # elif 'naver' in brand:
    #     #     value = brand
    #     # elif 'gmarket' in brand:
    #     #     value = brand
    #     # elif 'lotteimall' in brand:
    #     #     value = brand
    #     # elif 'interpark' in brand:
    #     #     value = brand
    #     # query = f'''
    #     # UPDATE test1
    #     # SET brand {value}
    #     # '''
    #     if 'coupang' in brand or 'ssg' in brand or '11st' in brand or 'auction' in brand or 'ohou' in brand or 'naver' in brand or 'gmarket' in brand or 'lotteimall' in brand or 'interpark' in brand:
    #         value = brand

    #     if value:
    #         query = f"UPDATE {table_name} SET brand = '{value}' WHERE column_name = 'brand'"
    #         execute_query(query)

    # url
    try:
        col = eval(data)
        if len(col) == 2: # 이미지 수집이 완료된 url
            prd_url = col[0]
            prd_status = col[1]
            query = f"INSERT INTO {table_name} (url, status) VALUES ('{prd_url}', '{prd_status}')"
            execute_query(query)

    except:
        query = f"INSERT INTO {table_name} (url) VALUES ('{data}')"
        execute_query(query)
    cnt += 1
    print(f'{cnt}/{len(csv_data)}')


# check check check check check check
# query = f"select * from {table_name} limit 5;"
# execute_query(query)


# insert status
check_list = ['패스','스캔필요']

check = random.choice(check_list)

if check == '패스':
    query = '''
    UPDATE test1
    SET status = 'pass' Where column_name = 'status'
    '''
elif check == '스캔필요':
    query = '''
    UPDATE test1
    SET status = 'scan' Where column_name = 'status'
    '''    
execute_query(query)


# check check check check check check
query1 = "show tables;"
execute_query(query1)

# check check check check check check
query2 = "SELECT * FROM test1 LIMIT 20;"
execute_query(query2)


# insert start_date
# insert end_date
# insert duration

# url이 11번가 인 것만 찾을 수 있는가....

# 쿼리 실행
# select_query = f"SELECT url FROM {table_name} WHERE url LIKE '%11st%'"
# conn = pymysql.connect(host='121.254.162.132',port = 3306, user='capture', password='edf@@0907', charset='utf8', db = 'edf_capture',use_unicode=True) 

# cursor = conn.cursor()
# cursor.execute(select_query)
# results = cursor.fetchall()

# # 결과 데이터를 새로운 테이블에 삽입
# insert_query = f"INSERT INTO '11st' (url) VALUES (%s)"
# cursor.executemany(insert_query, results)

# # 커밋
# conn.commit()






