import os
import shutil
import time

current_directory = os.getcwd()
file_list = os.listdir(current_directory)
file_list = [file for file in file_list if file.endswith('.jpg')]


for file_name in file_list:
    file_name = file_name.split('_')[0]
    brands = ['cou','sin','gmarket','auction','llst','interpark','naver','lotte','today']
    for brand in brands:
        if brand == file_name:
            os.mkdir(brand)
            print('done')
        break

            
   
