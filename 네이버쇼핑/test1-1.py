# # jamo 버전

# from jamo import h2j, j2hcj

# word = '만두'
# jamo_str = j2hcj(h2j(word))
# list = [i for i in word]

# print(jamo_str)
# print(list)




for i in range(1,5):
    img = f'{i}.PNG'
    pyautogui.moveTo(f'{i}.PNG')
    img = pyautogui.locateCenterOnScreen(f'{i}.PNG')
    time.sleep(1)
    if i == 2:
        pyautogui.doubleClick(img)
    else:
        pyautogui.click(img)
    print(i)

import time
import pyautogui
pyautogui.moveTo(x=1640,y=1050)
pyautogui.click()
pyautogui.moveTo(x=1660,y=1020)
pyautogui.click()
pyautogui.moveTo(x=820,y=320)
pyautogui.click()
pyautogui.moveTo(x=1100,y=280)
pyautogui.click()

