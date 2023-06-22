import csv

# CSV 파일 경로
file_path = "cou_list__.csv"

# CSV 파일 열기
with open(file_path, "r") as csv_file:
    # CSV 파일 읽기
    csv_reader = csv.reader(csv_file)
    data = list(csv_reader)  # CSV 데이터를 리스트로 변환

# data = data[0]
# print(data)
# print(len(data))
print(int((len(data[0])/3)*1))
print(int((len(data[0])/3)*2))
print(int((len(data[0])/3)*3))

print(len(data[0]))
list1 = data[0][:int((len(data[0])/3)*1)]
list2 = data[0][len(list1):int((len(data[0])/3)*2)]
list3 = data[0][len(list1+list2):int((len(data[0])/3)*3)]


print(len(list1))
print(len(list2))
print(len(list3))

# for i in list1:
with open('list1.csv' , "w", newline="") as csv_file:
    # CSV 파일 작성자 생성
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(list1)

with open('list2.csv' , "w", newline="") as csv_file:
    # CSV 파일 작성자 생성
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(list1)

# # for i in list2:
#     with open('list2.csv' , "w", newline="") as csv_file:
#         # CSV 파일 작성자 생성
#         csv_writer = csv.writer(csv_file)
#         csv_writer.writerows(i)




# print(len(a))


# new_file_path = 'tt.csv'

# with open(new_file_path , "w", newline="") as csv_file:
#     print('ck1')
#     # CSV 파일 작성자 생성
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerows(a)

# x = 0
# for i in data:
#     for j in range(1,4):
#         file = [data[0][x:int((len(data[0])/3)*j)]]
#         x = len(file[0])
#         print(x,int((len(data[0])/3)*j))
#         new_file_path = f'cou_{j}.csv'
#         with open(new_file_path , "w", newline="") as csv_file:
#             # CSV 파일 작성자 생성
#             csv_writer = csv.writer(csv_file)
#             csv_writer.writerows(file)
#         print(j)


    




        


