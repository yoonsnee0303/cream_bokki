

import pymysql
from sqlalchemy import create_engine

conn = pymysql.connect(host='121.254.162.132',port = 3306, user='capture', password='edf@@0907', charset='utf8') # db= 'edf_capture'
db_host = '121.254.162.132'
db_user = 'capture'
db_password = 'edf@@0907'
db_name = 'edf_capture'

# # 커서를 생성합니다
# cursor = conn.cursor()

# query = "show databases"
# cursor.execute(query)

# result = cursor.fetchall()

# # 결과를 출력합니다
# for row in result:
#     print(row[0])

# query2 = "use edf_capture"

# cursor.execute(query2)

# result = cursor.fetchall()

import pandas as pd

csv_file_path = 'test.csv'  # 업로드할 CSV 파일의 경로와 파일명
df = pd.read_csv(csv_file_path)
print(df.head())

# 데이터프레임의 데이터를 MySQL 데이터베이스에 업로드합니다
engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
table_name = 'bbang_ba_bo'  # 업로드할 테이블명
df.to_sql(name=table_name, con=conn, if_exists='replace', index=False)



# 쿼리를 실행합니다
# query = "SELECT * FROM 테이블명"
# cursor.execute(query)

# sql = "SELECT * FROM edf_capture"

# with conn:
#     with conn.cursor() as cur:
#         cur.execute(sql)
#         result = cur.fetchall()
#         for data in result:
#             print(data)


# cur =conn.cursor()
# print(cur.execute("SELECT test"))

#cur.execute("CREATE TABLE test(test char(10))")
# cur.execute("INSERT INTO test VALUES('test123')")
# conn.commit()
# conn.close()
# sql = 'INSERT into members values(%s)'

# test = 'string_input_test'

# vals = (test)
# cur.execute(sql,vals)
# conn.commit()
# conn.close()

# sql = 'select * from departments where department_test=%s'
# vals = (department_test)