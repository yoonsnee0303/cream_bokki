import requests
from bs4 import BeautifulSoup as bs
import json

pdt_lists = []
for pg in range(1,51):
    url = f'https://shopping.interpark.com/niSearch/shop/listPrdChoiceAndNormal.json?page={pg}&keyword=%EB%8F%99%EC%84%9C%EC%B9%B4%EC%82%B4%EB%9D%BC&rows=52&_=1687334655734' #1~50 #rows 고쳐보기


    req = requests.get(url,verify=False)
    data = json.loads(req.text)

# file_path = 'test.json'

# Open the file in write mode
# with open(file_path, 'w',encoding='utf-8') as file:
#     # Write the data to the file in JSON format
#     json.dump(data, file)


    print('페이지:',pg)
    try:
        for cnt in range(52):
            info = data['data']['listChoiceAndNormal'][cnt] # 30개까지
            for i in info:
                pdt_lists.append(info['name'])
            print('받아온 상품개수:', len(pdt_lists))
    except:
        for cnt in range(31):
            info = data['data']['listChoiceAndNormal'][cnt] # 30개까지
            for i in info:
                pdt_lists.append(info['name'])
            print('받아온 상품개수:', len(pdt_lists))

pdt_lists = list(set(pdt_lists))

print(len(pdt_lists))


file_path = 'test.txt'

with open(file_path, 'w',encoding='utf-8') as file:
    for item in pdt_lists:
        file.write(item + '\n')







