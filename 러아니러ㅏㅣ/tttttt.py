import pandas as pd
import pymysql
conn = pymysql.connect(host='121.254.162.132', port=3306, user='capture', password='edf@@0907', charset='utf8mb4', db='edf_capture', conv={'charset':'utf8mb4', 'use_unicode': True, 'sql_mode': 'PIPES_AS_CONCAT'})
# start_date 삽입




table_name = 'table1'

class update_db:
    def __init__(self,check,url):
        self.check = check
        self.url = url
        
    def 실행(self,sql_statements):

        try:
            cursor = conn.cursor()

            url_lists = []
            for sql in sql_statements:
                cursor.execute(sql)

                # Fetch all the rows (if app-cable)
                rows = cursor.fetchall()

                for row in rows:
                    # print(row)
                    url_lists.append(row[0]) # tuple로 출력되므로 [0]을 반드시 붙여야햠.
                row_count = len(rows)
                print("행의 개수:", row_count)

            # 파일저장
            # filename = 'all_list.csv'
            # import csv
            # with open(filename, 'w', newline='') as csvfile:
            #     writer = csv.writer(csvfile)
            #     writer.writerow([i[0] for i in cursor.description])  # 헤더 작성
            #     writer.writerows(rows)  # 행 작성

        finally:
            # Close the conn
            conn.close()
            print(len(url_lists))
        
        return url_lists
    
    def 상세페이지리스트(self):
        sql_statements = f'select url from {table_name} where start_date is null;'
        self.실행(sql_statements)
    
    def 패스여부(self):
        if self.check == '동서가구':
            sql_statements = f'UPDATE {table_name} SET status = "pass" WHERE url LIKE {self.url};'
        else:
            sql_statements = f'UPDATE {table_name} SET status = "nonpass" WHERE url LIKE {self.url};'

        self.실행(sql_statements)

    def 시간업데이트(self):
        sql_statements = f'UPDATE {table_name} SET start_date = current_timestamp() WHERE url LIKE {self.url}'
        self.실행(sql_statements)


# update = update_db()
# update.상세페이지리스트()

# update.패스여부(check,url)

# update.시간업데이트(url)

df_lists = []
df = pd.read_csv('test.csv')
test= df['url'].to_list()
print(len(test))

 
# prepare a cursor object using cursor() method
cursor = conn.cursor()
 
# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")
 
# Fetch a single row using fetchone() method.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# disconnect from server
conn.close()




