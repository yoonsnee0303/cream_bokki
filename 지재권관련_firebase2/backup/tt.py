import os
from openpyxl import Workbook

def create_excel_file():
    brands = ['신세계','지마켓','인터파크','11번가','오늘의집','롯데온','스마트스토어','옥션']
    for brand in brands:
        folder_path = f"C:/Users/Data2/OneDrive/바탕 화면/firebase2/{brand}/"
        output_file = f"{brand}_index.xlsx"

        file_list = os.listdir(folder_path)
        new_file_list = []
        for file in file_list:
            try:
                file = file.split('_')[3].split('.')[0]
            except:
                print('except')
                print(brand)
                print(file)

            if brand == "신세계":
                http = 'https://www.ssg.com/item/itemView.ssg?itemId='

            elif brand == "지마켓":
                http = 'http://item.gmarket.co.kr/Item?goodscode='

            elif brand == "인터파크":
                http = 'https://shopping.interpark.com/product/productInfo.do?prdNo='
                
            elif brand == "11번가":
                http = 'https://www.11st.co.kr/products/'

            elif brand == "오늘의집":
                http = 'https://ohou.se/productions/'

            elif brand == "롯데온":
                http = 'https://www.lotteimall.com/goods/viewGoodsDetail.lotte?goods_no='

            elif brand == "스마트스토어":
                http = 'https://smartstore.naver.com/newdf2013/products/'

            elif brand == "옥션":
                http = 'http://itempage3.auction.co.kr/DetailView.aspx?itemno='

            new_file_list.append(http+file)

        workbook = Workbook()
        sheet = workbook.active
        for index, file in enumerate(new_file_list):
            sheet.cell(row=index+1, column=1, value=file)

        workbook.save(output_file)
        print(f"{brand}Excel file '{output_file}' created successfully.")

create_excel_file()

