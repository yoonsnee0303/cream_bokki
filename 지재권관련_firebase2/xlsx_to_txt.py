import os

brands = ['11번가', '롯데온', '스마트스토어', '신세계', '오늘의집', '옥션', '인터파크', '지마켓', '쿠팡']

for brand in brands:
    file_path = f'C:/Users/Data2/OneDrive/바탕 화면/firebase2/{brand}'
    os.chdir(file_path)
    current_folder = os.getcwd()
    file_list = [file for file in os.listdir(current_folder) if file != 'desktop.ini'] # desktop.ini생략
    with open(f'../{brand}.txt', 'w') as file:
        file.write('\n'.join(file_list))
