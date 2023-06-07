import os
import shutil
import time

current_directory = os.getcwd()
file_list = os.listdir(current_directory)
file_list = [file for file in file_list if file.endswith('.pdf')]


for file_name in file_list:
    current_directory = os.getcwd()
    file_list = os.listdir(current_directory)

    if 'test.py' in file_name:
        continue
    
    storage_folder_name = file_name.split('___')[0]
    producer_folder_name = file_name.split('___')[1]

    
    if storage_folder_name in file_list:
        shutil.copy(file_path, new_path)
        print(f"Copied {file_name} to {new_path}")
    
    else:
        os.chdir(os.path.join(current_directory,'')) # change dir
        os.mkdir(storage_folder_name)
        print(f"Created new folder: {storage_folder_name}")
        file_path = os.path.join(current_directory, file_name)
        new_path = os.path.join(current_directory, storage_folder_name,'')  # ''은 역슬래시만 붙게 됨
        print(new_path)
        shutil.copy(file_path, new_path)
        print(f"Copied {file_name} to {new_path}")
        # os.chdir('../')


    if producer_folder_name in file_list:
        shutil.copy(file_path, new_path)
        print(f"Copied {file_name} to {new_path}")

    else:
        os.chdir(os.path.join(current_directory,'')) # change dir
        os.mkdir(producer_folder_name)
        print(f"Created new folder: {producer_folder_name}")
        file_path = os.path.join(current_directory, file_name)
        new_path = os.path.join(current_directory, producer_folder_name,'') # ''은 역슬래시만 붙게 됨
        shutil.copy(file_path, new_path)
        print(f"Copied {file_name} to {new_path}")
        # os.chdir('../')



    
    # file_path = os.path.join(current_directory, file_name)
    # new_path = os.path.join(current_directory, producer_folder_name, file_name)
    
    # shutil.copy(file_path, new_path)
    # print(f"Copied {file_name} to {new_path}")

    # break
