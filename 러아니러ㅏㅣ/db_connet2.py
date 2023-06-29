import pymysql

# conn = pymysql.connect(host='121.254.162.132', port=3306, user='capture', password='edf@@0907', charset='utf8', db='edf_capture')
conn = pymysql.connect(host='121.254.162.132', port=3306, user='capture', password='edf@@0907', charset='utf8mb4', db='edf_capture', conv={'charset':'utf8mb4', 'use_unicode': True, 'sql_mode': 'PIPES_AS_CONCAT'})


# sql_statements = [
#     'SHOW DATABASES;',
#     'USE edf_capture;',
#     '''CREATE TABLE bbang_ttol (
#         url varchar(255) not null,
#         status varchar(10) null,
#         date date null);''',
#     'show tables;'
# ]

# sql_statements = [
#     'insert into bbang_ttol values ("test",null, null);'
# ]

# sql_statements = [
#     'desc bbang_ttol;'
# ]


# sql_statements = [
#     # 'show tables;'
#     'Select * from table1;'
# ]

# sql_statements = [
    # 'select * from table1;',
    # 'desc table1;'
# ]




# sql_statements = [
#     'show databases;'
# ]

# sql_statements = [
#     "DELETE FROM table1 where url like '%%11st%%';"
# ]

# sql_statements = [
    # 'drop table table1;'
# ]

# sql_statements = [
#     'SELECT @@version;'
# ]

# sql_statements = [
#     'USE edf_capture;',
#     'insert into bbang_ba'
# ]

# sql_statements = [
# 'drop table if exists table1;',
# '''create table table1 (
#     brand varchar(50) not null,
#     url varchar(100) not null,
#     status varchar(50) null,
#     start_date datetime null,
#     end_date datetime null
# )'''
# ]

# sql_statements = [
    # 'select * from bbang_ttol;',
    # 'desc bbang_ttol;'
    # 'select * from table1;',
    # 'desc table1;'
# ]


sql_statements = [
    # "DELETE FROM bbang_ttol where url like '%%coupang%%';",
    'select * from bbang_ttol;',
]


try:
    # Create a cursor object
    cursor = conn.cursor()

    # Execute each SQL statement separately
    for sql in sql_statements:
        cursor.execute(sql)

        # Fetch all the rows (if app-cable)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
        row_count = len(rows)
        print("행의 개수:", row_count)

    # save to csv file
    filename = '테이블명.csv'
    import csv
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([i[0] for i in cursor.description])  # 헤더 작성
        writer.writerows(rows)  # 행 작성

finally:
    # Close the connection
    conn.close()
