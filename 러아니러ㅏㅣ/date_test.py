import pymysql

# sql_statements = ['''CREATE TABLE test3 (
# url varchar(255) not null,
# status varchar(10) null,
# date datetime,
# date2 datetime);''']

# sql_statements = ['desc test3;']
# sql_statements = ['INSERT INTO test3 (date) values (current_timestamp());']
sql_statements = ['select * from test3;']



conn = pymysql.connect(host='121.254.162.132', port=3306, user='capture', password='edf@@0907', charset='utf8mb4', db='edf_capture', conv={'charset':'utf8mb4', 'use_unicode': True, 'sql_mode': 'PIPES_AS_CONCAT'})


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
            print(row)
            # url_lists.append(row[0]) # tuple로 출력되므로 [0]을 반드시 붙여야햠.
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
