import csv

# CSV 파일 경로
file_path = "cou_test.csv"

# CSV 파일 열기
with open(file_path, "r") as csv_file:
    # CSV 파일 읽기
    csv_reader = csv.reader(csv_file)
    data = list(csv_reader)  # CSV 데이터를 리스트로 변환


print(len(data[0]))
list1 = data[0][:int(len(data[0])/2)]
list2 = data[0][int(len(data[0])/2):]


print(len(list1))
print(len(list2))



# for i in list1:
with open('list1.csv' , "w", newline="") as csv_file:
    # CSV 파일 작성자 생성
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows([list1])

with open('list2.csv' , "w", newline="") as csv_file:
    # CSV 파일 작성자 생성
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows([list2])

# # for i in list2:
#     with open('list2.csv' , "w", newline="") as csv_file:
#         # CSV 파일 작성자 생성
#         csv_writer = csv.writer(csv_file)
#         csv_writer.writerows(i)







    




        


