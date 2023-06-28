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

sql_statements = [
    'select * from table1;',
    'desc table1;'
]




# sql_statements = [
#     'show databases;'
# ]

# sql_statements = [
#     "DELETE FROM table1 where url like '%%11st%%';"
# ]

# sql_statements = [
#     'drop table table1;'
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
#     'select * from table1;',
#     'desc table1;'
# ]


# sql_statements = [
#     "DELETE FROM table1 where url like '%%11st%%';",
#     'select * from table1;',
# ]


try:
    # Create a cursor object
    cursor = conn.cursor()

    # Execute each SQL statement separately
    for sql in sql_statements:
        cursor.execute(sql)

        # Fetch all the rows (if app-cable)
        rows = cursor.fetchall()

        # Print the fetched rows
        for row in rows:
            print(row)

finally:
    # Close the connection
    conn.close()
