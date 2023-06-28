conn = pymysql.connect(host='121.254.162.132',port = 3306, user='capture', password='edf@@0907', charset='utf8', db = 'edf_capture',use_unicode=True) 

cursor = conn.cursor()

use_db_query = '''
    desc table1;
'''

# drop table if exists test1;
# del_table_sql = '''
# create table table1 (
#     brand varchar(50) not null,
#     url varchar(100) not null,
#     status varchar(50) null,
#     start_date Date null,
#     end_date Date null
# )
# '''
cursor.execute(use_db_query)
conn.commit()
rows = cursor.fetchall()
for row in rows:
    print(row)