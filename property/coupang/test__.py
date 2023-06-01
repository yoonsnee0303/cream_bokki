import csv
# #list_test txt파일로 저장
# with open('cou_list.txt', 'w', newline='', encoding='utf-8-sig') as f:
#     write = csv.writer(f)
#     write.writerows([lists])

with open('cou_list.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        lists = row
        # row.replace('[','').replace(']','').replace("'")
        print(row[1161])
        print(type(row))
# lists = list(map(list, zip(*csv_list)))
# for i in range(len(lists)):
#     if lists[i][0].count('스캔필요') + lists[i][0].count('패스') == 0:
#         start_cnt = i
#         break