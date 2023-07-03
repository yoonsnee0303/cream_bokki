import pymysql

# conn = pymysql.connect(host='121.254.162.132', port=3306, user='capture', password='edf@@0907', charset='utf8', db='edf_capture')
conn = pymysql.connect(host='121.254.162.132', port=3306, user='capture', password='edf@@0907', charset='utf8mb4', db='edf_capture', conv={'charset':'utf8mb4', 'use_unicode': True, 'sql_mode': 'PIPES_AS_CONCAT'})


# sql_statements = [
#     'SHOW DATABASES;',
#     'USE edf_capture;',
    # '''CREATE TABLE test2 (
    #     url varchar(255) not null,
    #     status varchar(10) null,
    #     date timestamp null default current_timestamp);''',
    # 'show tables;',
    # 'desc test2;'
# ]

# sql_statements = [
#     'insert into bbang_ttol values ("test",null, null);'
# ]

# sql_statements = [
#     'desc bbang_ttol;'
# ]


# sql_statements = [
    # 'show tables;'
    # 'desc table1;'
    # 'select * from table1;'
# ]

# sql_statements = [
    # 'UPDATE table1 SET status = "pass" WHERE status'
# ]

# sql_statements = [
    # 'select * from table1;',
    # 'desc table1;'
# ]




# sql_statements = [
    # 'show databases;'
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


# sql_statements = [
    # 'UPDATE table1 SET status = "pass" WHERE url LIKE "%B589608562%" ', # pass or nonpass
    # 'UPDATE table1 SET DATE3 = current_timestamp() WHERE url LIKE "%B589608562%" ', # insert date
    # 'ALTER TABLE table1 ADD date3 timestamp null default current_timestamp;',  # date 컬럼 삽입
    # 'ALTER TABLE table1 DROP COLUMN Date;', # 컬럼 삭제
    # 'ALTER TABLE table1 CHANGE date3 start_date timestamp;', # 컬럼 이름 변경
    # "alter table table1 modify Date date null ;", # 타입변경 (int(11) -> date)
    # 'ALTER TABLE table1 ADD COLUMN end_date VARchar(20) DEFAULT CURRENT_TIMESTAMP;',
    # 'UPDATE table1 SET end_date = current_timestamp() WHERE url LIKE "%B589608562%" ',
    # 'SELECT TIMESTAMPDIFF(SECOND, start_date, end_date) AS duration FROM table1',
    # 'desc table1;',
    # 'select * from table1',
    # 'select url from table1 where start_date is not null;' # 원래는 null이여야함
# ]


# sql_statements = [
    # "DELETE FROM bbang_ttol where url like '%%interpark%%';",
    # 'select * from bbang_ttol;',
# ]



try:
    # Create a cursor object
    cursor = conn.cursor()
    
    
    url_lists = []
    # Execute each SQL statement separately
    for sql in sql_statements:
        cursor.execute(sql)

        # Fetch all the rows (if app-cable)
        rows = cursor.fetchall()

        for row in rows:
            # print(row)
            url_lists.append(row[0]) # tuple로 출력되므로 [0]을 반드시 붙여야햠.
        row_count = len(rows)
        print("행의 개수:", row_count)

    # save to csv file
    # filename = 'all_list.csv'
    # import csv
    # with open(filename, 'w', newline='') as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow([i[0] for i in cursor.description])  # 헤더 작성
    #     writer.writerows(rows)  # 행 작성

finally:
    # Close the conn
    conn.close()
    print(url_lists)
