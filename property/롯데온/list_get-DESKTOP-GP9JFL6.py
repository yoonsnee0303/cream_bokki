import requests
import csv
import json

url = 'https://www.lotteimall.com/search/searchMain.lotte?isTemplate=Y&headerQuery=장인가구&colldisplay=3200'
response = requests.get(url)

json_data = response.json()
# print(json_data)
# print(type(json_data))

# temp = json_data['body'][15]['data'][0]['wishListMap']['goods_no']
temp = json_data['body'][16]['data'] # 15
# print(len(temp))
item_list = []

for i in range(len(temp)):
    EA_url = 'https://www.lotteimall.com/goods/viewGoodsDetail.lotte?goods_no=' + str(temp[i]['wishListMap']['goods_no'])
    item_list.append(EA_url)
    print(i+1)

#list_test csv파일로 저장
with open('lot_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
    write = csv.writer(f)
    write.writerows([item_list])