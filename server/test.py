import pymysql

info = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'0000',
    'db':'soloDB',
    'charset':'utf8'
}

conn = pymysql.connect(**info)
cur = conn.cursor()


# quary = '''
# create table userTable(
#     id char(4),
#     userName char(15),
#     email char(20),
#     birthYear int
# )
# '''

quary1 = '''
insert into userTable values ('hong', '홍지윤', 'hong@naver.com', 1996);
'''

quary2 = '''
insert into userTable values ('kim', '김태연', 'kim@daum.net', 2011);
'''

quary3 = '''
insert into userTable values ('star', '별사랑', 'star@paran.com', 1990);
'''

quary4 = '''
insert into userTable values ('yang', '양지은', 'yang@gmail.com', 1993);
'''



cur.execute(quary1)
cur.execute(quary2)
cur.execute(quary3)
cur.execute(quary4)
conn.commit()
conn.close()