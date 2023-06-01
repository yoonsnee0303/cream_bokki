

import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://smartstore.naver.com/kndigitalstore/category/ALL?st=POPULAR&dt=LIST&page={}&size=80'
products = []

for page_num in range(1, 8):
    url = base_url.format(page_num)
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        product_tags = soup.find_all(class_='_1HA92CdeY4')
        img_tags = soup.find_all('img')
        for product_tag, img_tag in zip(product_tags, img_tags):
            product_name = product_tag.text
            img_url = img_tag.get('src')
            if img_url is not None:
                products.append({'name': product_name, 'img_url': img_url})
    else:
        print(f'Request failed for {url} with status code {response.status_code}')

df = pd.DataFrame(products)
df.to_excel('products.xlsx', index=False)




