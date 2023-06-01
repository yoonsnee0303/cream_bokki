test = [
['https://www.coupang.com/vp/products/5234697152?itemId=7625012746'],
['https://www.coupang.com/vp/products/52568464901?itemId=7460043525'],
['https://www.coupang.com/vp/products/52568464901?itemId=499198381'],
['https://www.coupang.com/vp/products/52568464901?itemId=499198501'],
['https://www.coupang.com/vp/products/52568464901?itemId=499198388'],
["https://www.coupang.com/vp/products/6310388973?itemId=13094972315&vendorItemId=80355859235"],
["https://www.coupang.com/vp/products/143085482?itemId=415669019&vendorItemId=4007678334"],
["https://www.coupang.com/vp/products/143085482?itemId=415669023&vendorItemId=4007678354"],
["https://www.coupang.com/vp/products/143085441?itemId=415668938&vendorItemId=4007350183"],
["https://www.coupang.com/vp/products/6785266940?itemId=15969898791&vendorItemId=83176014423"],
["https://www.coupang.com/vp/products/6785266831?itemId=15969898161&vendorItemId=83176014825"]]

import csv
with open('cou_list.csv', 'w', newline='', encoding='utf-8-sig') as f:
    write = csv.writer(f)
    write.writerows(test)

with open('cou_list.csv', 'r', newline='',encoding='utf-8-sig') as f:
    read = csv.reader(f)
    lists = list(read)

print(lists)
print(len(lists))
print(lists[0])
print(lists[0][0])
print()
print(lists[-1])