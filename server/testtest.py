import pymysql
import openpyxl

workbook = openpyxl.load_workbook('url.xlsx')
sheet = workbook.active
data = []

for row in sheet.iter_rows(values_only=True):
    data.append(row)

urls= list(data[0])


conn = pymysql.connect(host='121.254.162.132',port = 3306, user='capture', password='edf@@0907', charset='utf8', db = 'edf_capture') 

cursor = conn.cursor()

table_name = 'bbang_ttol'

cnt = 1
for column in urls:
    try:
        data = eval(column)
    except:
        pass
    if len(data) == 2: # [url,패스/스캔필요]
        prd_url = data[0]
        prd_status = data[1]
        query = f"INSERT INTO {table_name} (url, status) VALUES ('{prd_url}', '{prd_status}')"
        cursor.execute(query)
        conn.commit()

    elif len(data) == 1:
        # escaped_column = column.replace("'", "/").replace(",","/")
        query = f"INSERT INTO {table_name} (url) VALUES ('{column}')"
        cursor.execute(query)
        conn.commit()

    print(f'{cnt}/{len(urls)}')
    cnt += 1


conn.commit()

query = f"select * from {table_name} limit 5;"
cursor.execute(query)
conn.commit()

print('done')
