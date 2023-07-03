import pymysql
import random


conn = pymysql.connect(host='121.254.162.132', port=3306, user='capture', password='edf@@0907', charset='utf8mb4', db='edf_capture', conv={'charset':'utf8mb4', 'use_unicode': True, 'sql_mode': 'PIPES_AS_CONCAT'})

# sql_statements = [
    # "DELETE FROM bbang_ttol where url like '%%interpark%%';",
    # 'select * from table1;',
# ]

# create table
# sql_statements = [
#     '''CREATE TABLE table1 (
#         brand VARCHAR(50) NOT NULL,
#         url VARCHAR(100) NOT NULL,
#         status VARCHAR(50) NULL
#     )'''
# ]


# Date Date Date Date Date Date Date Date Date
# 특정 테이블의 컬럼 목록 가져오기
table_name = 'table1'
column_name = 'Date'
cursor = conn.cursor()
cursor.execute(f"DESCRIBE {table_name}")
columns = [row[0] for row in cursor.fetchall()]

if column_name in columns:
    print(f"The column '{column_name}' already exists.")
else:
    # 컬럼 추가 쿼리 실행
    cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} INT")

    # 변경 사항 커밋
    conn.commit()

    print(f"The column '{column_name}' has been added.")

# url = 'http://itempage3.auction.co.kr/DetailView.aspx?itemno=B330756835'
# check_lists = ['패스','스캔필요']
# check  = random.choice(check_lists)



# try:
#     # Create a cursor object
#     cursor = conn.cursor()

#     # Execute each SQL statement separately
#     for sql in sql_statements:
#         cursor.execute(sql)

#         # Fetch all the rows (if app-cable)
#         rows = cursor.fetchall()

#         for row in rows:
#             print(row)
#         row_count = len(rows)
#         print("행의 개수:", row_count)

# finally:
#     # Close the connection
#     conn.close()


