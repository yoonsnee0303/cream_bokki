import requests
import csv
import json
import time

url_data = []
for i in range(134):
    try:
        print(f'{i+1}/134')
        url = f'https://shopping.interpark.com/niSearch/shop/listPrdChoiceAndNormal.json?pis1=shop&page={i+1}&keyword=장인가구&rows=52'
        res = requests.get(url)

        data = json.loads(res.text)
        cnt = len(data['data']['listChoiceAndNormal'][0])
        for j in range(cnt+1):
            try:
                item_url = 'https://shopping.interpark.com/product/productInfo.do?prdNo=' + str(data['data']['listChoiceAndNormal'][j]['prdNo'])
                # print(f'{j}/{item_url}')
                # print(cnt)
                url_data.append(item_url)
            except:
                pass
    except:
        pass




#list_test csv파일로 저장
with open('inter_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
    write = csv.writer(f)
    write.writerows([url_data])